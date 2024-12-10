import asyncio 
from time import strftime
async def late(sec):
    s = strftime('%X')
    await asyncio.sleep(sec)
    return sec, s, strftime('%X')

async def main():
    print(*await asyncio.gather(late(3), late(2)))

asyncio.run(main())