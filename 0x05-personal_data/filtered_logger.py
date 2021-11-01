#!/usr/bin/env python3
"""Regex-ing
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Function that returns a log message obfuscated
    Use regex to replace occurrences of certain field values
    """
    for i in fields:
        message = re.sub(f'{i}=.+?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message
