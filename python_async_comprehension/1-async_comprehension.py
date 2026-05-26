#!/usr/bin/env python3
"""
This module contains a coroutine called async_comprehension.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously loop 10 times over async_generator using an
    async comprehension, returning the 10 random numbers.
    """
    return [number async for number in async_generator()]
