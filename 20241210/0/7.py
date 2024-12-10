import asyncio

async def prod(q1):
    for i in range(5):
        await asyncio.sleep(1)
        await q1.put(f"value_{i}")
        print(f"prod: put value_{i} to q1")
        


async def mid(q1, q2):
    while True:
        val = await q1.get()
        print(f"mid: got {val} from q1")
        await q2.put(val)
        print(f"mid: put {val} to q2")

async def cons(q2):
    while True:
        val = await q2.get()
        print(f"cons: got {val} from q2")

async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    ptask = asyncio.create_task(prod(q1))
    mtask = asyncio.create_task(mid(q1, q2))
    ctask = asyncio.create_task(cons(q2))
    await ptask

asyncio.run(main())