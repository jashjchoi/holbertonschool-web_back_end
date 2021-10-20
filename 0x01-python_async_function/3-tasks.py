#!/usr/bin/env python3
"""Import wait_random from 0-basic_async_syntax to create Tasks
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    (do not create an async function
    use the regular function syntax to do this)
    Write function task_wait_random that takes an integer max_delay
    Returns:
        asyncio.Task
    """
    queue = asyncio.get_event_loop()
    return queue.create_task(wait_random(max_delay))
