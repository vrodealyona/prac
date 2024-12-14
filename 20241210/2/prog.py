import asyncio
import random

async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await asyncio.gather(event_in1.wait(), event_in2.wait())
    B[start:finish] = A[start:middle] + A[middle:finish]
    event_out.set()

async def mtask(A):
    N = len(A)
    B = [0] * N
    tasks = []
    events = [asyncio.Event() for _ in range(N)]
    for length in range(1, N, length * 2):
        for i in range(0, N, length * 2):
            middle = min(i + length, N)
            finish = min(i + 2 * length, N)
            event_in1 = events[i]