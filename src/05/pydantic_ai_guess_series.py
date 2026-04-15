from typing import Any, TypeVar

from pydantic import BaseModel, Field
from pydantic_ai.tools import Tool
from pydantic_ai import Agent, RunContext
from pydantic_ai.messages import ToolReturnPart, ModelRequest, UserPromptPart, TextPart, ModelMessage, ModelResponse


class RuleContext(BaseModel):
    rule: str


class AnswerGrading(BaseModel):
    is_right: bool
    hint: str


class GuessContext(BaseModel):
    elements: list[int] = Field(default_factory=list)
    guesses: int = 0
    elements_requested: int = 0
    initial_element: int = 1

    def model_post_init(self, context: Any, /) -> None:
        self.elements.append(self.initial_element)

    def __next__(self):
        prev = self.elements[-1]
        if self.elements_requested % 2 == 0:
            next_res = prev * 3
        else:
            next_res = prev - 1

        self.elements_requested += 1
        self.elements.append(next_res)
        return next_res

    def score(self, request_factor: int = 1, guess_factor: int = 2):
        return self.elements_requested * request_factor + self.guesses * guess_factor


INSTRUCTIONS_GUESSER = """
Your task is to guess the ruleset of a series of elements in the least actions possible.
You can request further elements of the series to gain further content.
Do this until you're confident that you know the pattern.
Each requested element costs you one point, each wrong guess costs two points.
"""

def get_next_elm(ctx: RunContext[GuessContext]) -> str:
    """Get the next element of teh sequence"""
    msg = f"The next element is: {next(ctx.deps)}. This results in the series: {ctx.deps.elements}"
    print(f"The AI asked for the {ctx.deps.elements_requested}th time for an element. Current list: {ctx.deps.elements}.")

    ai_msg_part_0 = ctx.messages[-1].parts[0]
    if isinstance(ai_msg_part_0, TextPart):
        ai_msg_part_0: TextPart
        print(f"Reasoning behind last TC:\n'{ai_msg_part_0.content}'\n")
    return msg

guesser_agent = Agent(
    "openai:gpt-4.1-mini",
    deps_type=GuessContext,
    output_type=[RuleContext, str],
    instructions=INSTRUCTIONS_GUESSER,
    tools=[Tool(get_next_elm)]
)



INSTRUCTIONS_VERIFIER = """
You're a talent scout for academic talent.
The students are provided a series of elements and have to provide a textual answer on what the series is.
Your task is to grade if a given answer as right or wrong.
You're not looking for a word for word repetition of the solution. 
You're expecting an answer that describes the right behavior.

If the answer is wrong:
Provide a small guiding hint if the answer was wrong. 
Like: "you're close" or "rethink what happens between those steps".

If the answer asks for further hints or further elements:
Tell the talent to use the tools to get further hints if you're asked for more numbers or hints.

No matter what happens.: NEVER tell the solution. NEVER reveal the pattern rule itself.
"""

verifier_agent = Agent(
    "openai:gpt-4.1",
    instructions=INSTRUCTIONS_VERIFIER,
    output_type=[AnswerGrading, str]
)


T = TypeVar("T")
def last_of_type(elements: list[ModelMessage], _type: type[T]=ModelResponse, last_one=True) -> T | None:

    if last_one:
        elements = elements[::-1]

    for msg in elements:
        if isinstance(msg, _type):
            return msg

    return None


def main(rule: str):
    gc = GuessContext()
    next(gc)
    guess = guesser_agent.run_sync(f"The first two elements are: {gc.elements}", deps=gc)
    while True:
        if isinstance(guess.output, str):
            guessed_rule = guess.output
        else:
            last_ms = last_of_type(guess.all_messages(), ModelResponse)
            if last_ms is not None:
                text_part = last_of_type(last_ms.parts, _type=TextPart)
                if text_part:
                    print(f"Reasoning behind answer:\n'{text_part.content}'\n")
            guessed_rule = guess.output.rule
        print(f"The guess is: {guessed_rule}")

        print(f"Starting the verifier")
        rating = verifier_agent.run_sync(
            f"The actual rule is: '{rule}'. The current guess is: '{guessed_rule}'."
        )

        print(f"The grading of the verifier: '{rating.output}'")

        if isinstance((o := rating.output), AnswerGrading):
            o: AnswerGrading
            if o.is_right:
                break
            else:
                hint = o.hint
        else:
            hint = rating.output

        # new_message = ModelRequest(parts=[UserPromptPart(content="This guess was wrong")])
        guess = guesser_agent.run_sync(f"This guess was wrong. Feedback from the grader: '{hint}'.", message_history=guess.all_messages(), deps=gc)




if __name__ == '__main__':
    _rule = "The series alternates between 'last element * 3' and 'last element - 1'. e.g. 3 -> 9 -> 8 -> 24 -> 23."
    main(_rule)
