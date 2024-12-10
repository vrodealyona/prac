import asyncio 
from time import strftime
async def late(sec):
    s = strftime('%X')
    await asyncio.sleep(sec)
    return sec, s, strftime('%X')

async def main():
    print(*await late(1))
    print(*await late(2))
    task3 = asyncio.create_task(late(3))
    task4 = asyncio.create_task(late(4))
    print(*await task3)
    print(*await task4)

asyncio.run(main())