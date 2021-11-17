#!/usr/bin/env python3
"""Auth class"""

from db import DB
from typing import TypeVar, Union
from user import User
import bcrypt


def _hash_password(password: str) -> str:
    """Takes in a password string arguments and returns bytes"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
