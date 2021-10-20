#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Import async_comprehension from the previous file and
    write a measure_runtime coroutine
    that will execute async_comprehension four times in
    parallel using asyncio.gather
    Return:
        measure the total runtime
    """
    t1 = time.perf_counter()
    num = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*num)
    t2 = time.perf_counter()
    return t2 - t1
