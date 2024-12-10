import asyncio

evsnd = asyncio.Event()
evmid0 = asyncio.Event()
evmid1 = asyncio.Event()

async def snd():
    print("snd: generated evsnd")
    evsnd.set()

async def mid(event, k):
    await evsnd.wait()
    print(f"mid({k}): received evsnd")
    print(f"mid({k}): generated evmid{k}")
    event.set()

async def rcv():
    await evmid0.wait()
    print("rcv: received evmid0")
    await evmid1.wait()
    print("rcv: received evmid1")



async def main():
    await asyncio.gather(
        rcv(),
        mid(evmid1, 1),
        mid(evmid0, 0),
        snd()
    )

asyncio.run(main())