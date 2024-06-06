#!/usr/bin/env python3
''' This module defines a function '''

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' returns the first element in the list '''

    if lst:
        return lst[0]
    else:
        return None
