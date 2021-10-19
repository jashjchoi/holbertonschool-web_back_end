#!/usr/bin/env python3
"""type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument
    returns a function that multiplies a float by multiplier
    Returns:
        Callable[[float], float]: [description]
    """
    return lambda x: x * multiplier
