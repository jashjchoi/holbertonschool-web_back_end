#!/usr/bin/env python3
"""TypeVar; More involved type annotations
"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Given the parameters and the return values,
    add type annotations to the function
    Returns:
        Union[Any, T]: value in key of dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
