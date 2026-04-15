import json
import random
from pathlib import Path

from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from pydantic_ai.agent import AgentRunResult
from pydantic_ai.messages import ModelMessage, ModelRequest
from pydantic_ai.tools import Tool
from pydantic_ai.usage import UsageLimits
from pydantic_core import to_jsonable_python


class DiceResult(BaseModel):
    result: int

def throw_a_dice(ctx: RunContext, lower_limit: int, upper_limit: int) -> DiceResult:
    """throw a dice with a certain interval of numbers, limits are included"""
    r = random.randint(lower_limit, upper_limit)
    print(f"Dice called using {lower_limit=}, {upper_limit=} and got {r} as result")
    return DiceResult(result=5)

def log_msgs(hist: list[ModelMessage]) -> list[ModelMessage]:
    dump = to_jsonable_python(hist)
    Path(f"log-file.json").write_text(json.dumps(dump, indent=4))
    return hist

dice_agent = Agent(
    "openai:gpt-4.1",
    instructions="You're Dice-GPT. You handle fair dice rolls.",
    output_type=[DiceResult, str],
    tools=[Tool(throw_a_dice)],
    history_processors=[log_msgs]
)

res = dice_agent.run_sync("throw a dice between 10 and 20")

print(res.all_messages())
print(res.output)
print(repr(res.output))