#!/usr/bin/env python3
"""Async Comprehensions
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Import async_generator from the previous task
    then write a coroutine called async_comprehension that takes no arguments
    Returns:
        10 random float numbers
    """
    return [n async for n in async_generator()]
