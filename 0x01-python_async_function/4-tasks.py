#!/usr/bin/env python3
''' Defines a function '''

import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' spawns wait_random for n times '''

    wait_random = __import__('3-tasks').task_wait_random

    return sorted(await asyncio.gather(*(wait_random(max_delay)
                                         for i in range(n))))
