#!/usr/bin/env python3
"""type-annotated function sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ takes a list input_list of floats as argument
    Returns:
        float: return sum of all float number in a list
    """
    return float(sum(input_list))
