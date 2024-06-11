#!/usr/bin/env python3
''' Defines a function '''

from random import random
import asyncio


async def wait_random(max_delay=10):
    ''' waits for a random number of seconds and then returns it '''

    wait_time = random() * max_delay

    await asyncio.sleep(wait_time)

    return wait_time
