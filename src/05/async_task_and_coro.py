import asyncio
import time


async def sleep_token(name: str, st=1):
    print(f"[{name}] Before await")
    await asyncio.sleep(st)
    print(f"[{name}] After await")
    return name


async def main_tasks():
    """ create tasks """
    print("main_tasks()")
    task1 = asyncio.create_task(sleep_token("call1"))
    task2 = asyncio.create_task(sleep_token("call2"))

    print(type(task1))

    n1, n2 = await asyncio.gather(task1, task2)
    print(n1, n2)

async def main_await():
    """ create and wait coroutines (synchronous behaviour) """
    coro1 = sleep_token("call1")
    coro2 = sleep_token("call2", st=2)

    await coro2
    await coro1


async def wrap_main_await():
    """ fails on purpose """
    coro2 = main_tasks()
    print("OUT here!")
    x = await asyncio.gather(coro2)


async def main_block():
    """ demo to show that it's only one thread """
    task1 = sleep_token("call1", st=4)
    time.sleep(4)
    print(task1)
    res = await task1
    print(res)


asyncio.run(wrap_main_await())

