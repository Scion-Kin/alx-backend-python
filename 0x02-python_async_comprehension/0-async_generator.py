#!/usr/bin/env python3
''' This module defines a function '''

from random import random, randint


async def async_generator():
    ''' generates 10 random numbers '''

    for i in range(10):

        yield random() * randint(0, 10)
