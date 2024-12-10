import asyncio 

async def squarer(x):
    return x*x

async def doubler(x):
    return 2*x

async def main(x, y):
    async with asyncio.TaskGroup() as tg:
        tasks = tg.create_task(squarer(x), squarer(y))
    x, y = await asyncio.gather(squarer(x), squarer(y))
    x, y = await asyncio.gather(doubler(x), doubler(y))
    return x, y

print(*asyncio.run(main(2, 3)))