#!/usr/bin/env python3
"""
Module for async comprehension task.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using an async
    comprehension and returns them as a list of floats.
    """
    return [i async for i in async_generator()]
