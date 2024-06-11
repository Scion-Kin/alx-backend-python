#!/usr/bin/env python3
''' Defines a function '''

from typing import List
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' spawns wait_random for n times '''

    wait_random = __import__('0-basic_async_syntax').wait_random

    return sorted(await asyncio.gather(*(wait_random(max_delay)
                                         for i in range(n))))
