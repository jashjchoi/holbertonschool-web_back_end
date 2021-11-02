#!/usr/bin/env python3
"""Encrypting passwords
User passwords should NEVER be stored in plain text in a database
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted hashed password, which is a byte string"""
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )


def is_valid(hashed_password: bytes, password: str) -> bool:
    """expects 2 arguments and returns a boolean
    validate that the provided password matches the hashed password
    """
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed_password
    )
