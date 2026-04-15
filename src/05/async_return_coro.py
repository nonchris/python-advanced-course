import asyncio

"""
This example crashes and that's what to demonstrate
"""

async def async_function():
    await asyncio.sleep(1)
    print("Async function completed")

async def wrapper_function():
    task = async_function()
    return task

async def main():
    task = wrapper_function()

    print("After calling wrapper_function")

    await asyncio.sleep(2)

    await task

asyncio.run(main())
