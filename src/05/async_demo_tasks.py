import asyncio


async def async_function(name: str):
    print(f"[{name}] Before await")
    await asyncio.sleep(1)
    print(f"[{name}] After await")


async def main():
    task1 = asyncio.create_task(async_function("call1"))
    task2 = asyncio.create_task(async_function("call2"))

    await asyncio.gather(task1, task2)


asyncio.run(main())
