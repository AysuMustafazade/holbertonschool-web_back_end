#!/usr/bin/env python3
"""
This module provides a coroutine that collects random numbers using an asynchronous comprehension.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from an async generator using an async comprehension and returns them.
    """
    return [number async for number in async_generator()]
