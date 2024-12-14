import asyncio
from collections import deque

async def writer(q, delay):
    k = 0
    await asyncio.sleep(delay)
    #print("writer")
    while True:
        await q.put(f"{k}_{delay}")
        await asyncio.sleep(delay)
        k += 1
        

async def stacker(q, st):
    #print('stacker')
    while True:
        el = await q.get()
        await st.put(el)

async def reader(st, count, delay): 

    for _ in range(count):
        await asyncio.sleep(delay)
        print(await st.get())
        


async def main():
    del1, del2, del3, count = eval(input())
    q = asyncio.Queue()
    st = asyncio.Queue()
    
    task1 = asyncio.create_task(reader(st, count, del3))
    task2 = asyncio.create_task(writer(q, del1))
    task3 = asyncio.create_task(writer(q, del2))
    task4 = asyncio.create_task(stacker(q, st))
    await task1
    task2.cancel()
    task3.cancel()
    task4.cancel()

asyncio.run(main())