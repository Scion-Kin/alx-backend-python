#!/usr/bin/env python3
''' This module defines a function '''

from math import fsum
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    ''' Returns the sum of floating point numbers and integers '''

    return fsum(mxd_lst)
