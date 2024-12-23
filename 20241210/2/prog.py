import asyncio
import random

async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    if middle < finish:
        await event_in2.wait()

    i, j = start, middle
    b = start
    while i < middle and j < finish:
        if A[i] <= A[j]:
            B[b] = A[i]
            i += 1
        else:
            B[b] = A[j]
            j += 1
        b += 1

    while i < middle:
        B[b] = A[i]
        i += 1
        b += 1
    while j < finish:
        B[b] = A[j]
        j += 1
        b += 1
    event_out.set()

async def mtasks(A):
    array_copy = A[:]
    length = len(A)
    temp_array = [0] * length
    task_list = []
    event_list = [asyncio.Event() for _ in range(length)]

    for event in event_list:
        event.set()

    segment_size = 1
    swap_arrays = True

    while segment_size < length:
        new_events = []
        for start in range(0, length, 2 * segment_size):
            end_event = asyncio.Event()
            new_events.append(end_event)
            mid = min(start + segment_size, length)
            if mid < length:
                mid_event = event_list[mid // segment_size]
            else:
                mid_event = asyncio.Event()
                mid_event.set()

            if swap_arrays:
                task_list.append(merge(array_copy, temp_array, start, mid, min(start + 2 * segment_size, length), event_list[start // segment_size], mid_event, end_event))
            else:
                task_list.append(merge(temp_array, array_copy, start, mid, min(start + 2 * segment_size, length), event_list[start // segment_size], mid_event, end_event))

        swap_arrays = not swap_arrays
        event_list = new_events
        segment_size *= 2

    return task_list, array_copy

import sys
exec(sys.stdin.read())