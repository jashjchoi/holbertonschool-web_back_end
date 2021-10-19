#!/usr/bin/env python3
"""From the previous file, import wait_n into 2-measure_runtime.py"""
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Create a measure_time function with integers n and max_delay
    as arguments that measures the total execution
    time for wait_n(n, max_delay)
    Returns:
        total_time / n
    """
    t0 = time.time()
    asyncio.run(wait_n(n, max_delay))
    t1 = time.time()
    fulltime = t1 - t0
    return fulltime / n
