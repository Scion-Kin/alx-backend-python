#!/usr/bin/env python3
''' This module defines a function '''

from asyncio import gather
from time import time


async def measure_runtime():
    ''' measures the runtime of async_comprehension function '''

    comp = __import__('1-async_comprehension').async_comprehension
    start = time()
    await gather(*(comp() for i in range(4)))
    end = time()

    return end - start
