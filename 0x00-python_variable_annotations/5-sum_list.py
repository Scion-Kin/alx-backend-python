#!/usr/bin/env python3
''' This module defines a function '''

from typing import List
import math


def sum_list(input_list: List[float]) -> float:
    ''' Returns a sum of floating point numbers from a list '''

    return math.fsum(input_list)
