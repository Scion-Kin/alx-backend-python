#!/usr/bin/env python3
''' This module defines a function '''

from typing import Any, Mapping, TypeVar, Union


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None] = None)\
                     -> Union[Any, TypeVar('T')]:
    ''' returns a key in a given dictionary '''

    if key in dct:
        return dct[key]
    else:
        return default
