from pydantic_ai import Agent

agent = Agent('openai:gpt-4.1-mini', system_prompt='Be a helpful assistant.')

result = agent.run_sync('Tell me a joke.')
print(result.output)
#> Did you hear about the toothpaste scandal? They called it Colgate.

print(result.all_messages())