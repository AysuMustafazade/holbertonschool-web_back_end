#!/usr/bin/env python3
from 0-async_generator import async_generator


async def async_comprehension():
    """Async Comprehension that collects 10 random numbers using an async generator"""
    return [i async for i in async_generator()]
