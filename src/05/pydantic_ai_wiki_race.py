from pydantic import BaseModel, model_validator, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.usage import UsageLimits
import requests

url_template = "https://wikipedia.org/w/api.php?action=query&prop=links&pllimit=max&format=json&titles={}"

headers = {
    "User-Agent": "LectureExampleBot/1.0 (contact: bot@chris-ge.de)"
}


class WikiRaceTask(BaseModel):
    start: str
    target: str
    current_pool: list[str]
    chosen_words: list[str] = Field(exclude=True, default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def _fill_target_list_if_none(cls, data) -> None | dict:
        if data.get("current_pool") is None:
            data["current_pool"] = WikiRaceTask.get_word_pool(data["start"])

        return data

    @staticmethod
    def get_word_pool(word: str) -> None | list[str]:
        resp = requests.get(url_template.format(word), headers=headers)
        if resp.status_code != 200:
            return None

        available_words = extract_pages_from_response(resp.json())

        return available_words

    def get_current_words_formatted_prompt(self):
        return "The available words are: " + self.get_formatted_words()

    def get_formatted_words(self):
        return ", ".join(self.current_pool)


class WikiRaceResult(BaseModel):
    task: WikiRaceTask
    path: list[str]

system_prompt = """
You are a Data-analyst.
Your task is to find a chain of associations from one word to another.
For this task you can always choose one word from a provided pool.
You will then receive a new pool of words to select from based on your previous choice.
Think first before you make a choice. Respond using markdown. Always provide reasoning before making a tool call.
"""

wiki_agent = Agent(
    "openai:gpt-4o",
    deps_type=WikiRaceTask,
    output_type=[WikiRaceResult],
    instructions=system_prompt,
)

def extract_pages_from_response(resp: dict) -> list[str]:
    sub_d = resp["query"]["pages"]
    sub_list = sub_d[list(sub_d.keys())[0]]["links"]
    names = []
    for entry in sub_list:
        names.append(entry["title"])

    return names


@wiki_agent.tool
def choose_word(ctx: RunContext[WikiRaceTask], word: str) -> str:
    """
    Choose which word shall be the next in chain.
    It returns the new association pool based on that word.
    """
    print(f"The LLM requested the word: {word}")
    if word not in ctx.deps.current_pool:
        ans = f"The word '{word}' is not in the available pool."
        print(ans)
        return ans

    words = WikiRaceTask.get_word_pool(word)
    if words is None:
        ans = f"Something went wrong. Please choose again."
        return ans

    ctx.deps.chosen_words.append(word)

    ctx.deps.current_pool = words

    return "The available words are: " + " ".join(words)


def main(start: str, target: str):
    init = WikiRaceTask(start=start, target=target)
    print(f"The the start is: '{start}' target is: '{target}'")
    res = wiki_agent.run_sync(
        f"Your target is: '{target}'. Your current pool is: {init.get_formatted_words()}.",
        deps=init,
        usage_limits=UsageLimits(request_limit=10),
    )

    print(res)


async def main_iter(start: str, target: str):
    init = WikiRaceTask(start=start, target=target)

    nodes = []
    init_prompt = f"Your target is: '{target}'. Your current pool is: {init.get_formatted_words()}."
    async with wiki_agent.iter(init_prompt, deps=init) as agent_run:
        async for node in agent_run:
            # Each node represents a step in the agent's execution
            nodes.append(node)

    pass



if __name__ == '__main__':
    main("Barack_Obama", "Python_(programming_language)")
    # asyncio.run(main_iter("Barack_Obama", "Python (Programmiersprache)"))




