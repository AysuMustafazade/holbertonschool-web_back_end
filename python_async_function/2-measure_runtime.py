#!/usr/bin/env python3
wait_n= __import__('1-concurrent_coroutines').wait_n
import asyncio
import time

async def measure_runtime():
    start_time = time.time()
    delays = asyncio.run(wait_n(5, 10))
    end_time = time.time()
    print(f"Delays: {delays}")
    print(f"Total runtime: {end_time - start_time:.2f} seconds")
