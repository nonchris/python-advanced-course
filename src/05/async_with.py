import asyncio
import time


# class X:
#     def __await__(self):
#         print("huiii")

async def sleep_token(name: str, st=1):
    # y = await X()
    print(f"[{name}] Before await")
    await asyncio.sleep(st)
    print(f"[{name}] After await")
    return name


async def main():
    print(f"started at {time.strftime('%X')}")
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            sleep_token('call1'))

        task2 = tg.create_task(
            sleep_token("call2"))

        await asyncio.sleep(5)

    print(f"ended at {time.strftime('%X')}")

    print(task1.result())

asyncio.run(main())
