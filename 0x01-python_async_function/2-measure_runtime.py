#!/usr/bin/env python3
''' Defines a function '''

from time import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    ''' measures the time spent executing "wait_n" function '''

    wait_n = __import__('1-concurrent_coroutines').wait_n
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time() - start

    return end / n
