#!/usr/bin/env python3
''' This module defines a function '''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Returns a tuple containing every number in the list and it's length '''

    return [(i, len(i)) for i in lst]
