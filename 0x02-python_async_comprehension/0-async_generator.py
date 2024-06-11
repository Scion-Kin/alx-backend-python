#!/usr/bin/env python3
''' This module defines a function '''

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' generates 10 random numbers '''

    for i in range(10):

        await sleep(1)
        yield random() * 10
