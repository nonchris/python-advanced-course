import random

from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from pydantic_ai.tools import Tool


class DiceResult(BaseModel):
    result: int

def throw_a_dice(ctx: RunContext, lower_limit: int, upper_limit: int) -> int:
    """throw a dice with a certain interval of numbers, limits are included"""
    r = random.randint(lower_limit, upper_limit)
    print(f"Dice called using {lower_limit=}, {upper_limit=} and got {r} as result")
    return r

dice_agent = Agent(
    "openai:gpt-4.1",
    instructions="You're Dice-GPT. You handle fair dice rolls.",
    output_type=[DiceResult, str],
    tools=[Tool(throw_a_dice)]
)

res = dice_agent.run_sync("throw a dice between 10 and 20")

print(res.all_messages())
print(res.output)
print(repr(res.output))