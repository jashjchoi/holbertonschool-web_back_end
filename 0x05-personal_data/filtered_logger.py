#!/usr/bin/env python3
"""Regex-ing
"""

import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ('email', 'phone', 'ssn', 'password', 'name')


class RedactingFormatter(logging.Formatter):
    """class to accept a list of strings fields constructor argument
    Implement the format method to filter values in incoming log records
    using filter_datum
    Values for fields in fields should be filtered.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """method to filter values in incoming log records"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Function that returns a log message obfuscated
    Use regex to replace occurrences of certain field values
    """
    for i in fields:
        message = re.sub(f'{i}=.+?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """Implement a get_logger function that takes no arguments
    and returns a logging.Logger object
    """
    user_data = logging.getLogger("user_data")
    user_data.setLevel(logging.INFO)
    user_data.propagate = False
    handler = logging.StreamHandler()
    formatter = logging.Formatter(RedactingFormatter(PII_FIELDS))
    handler.setFormatter(formatter)
    user_data.addHandler(handler)
    return user_data


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to secure holberton database to read a users table
    The database is protected by a username and password
    that are set as environment variables on the server named
    """
    user = os.getenv('PERSONAL_DATA_DB_USERNAME')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD')
    host = os.getenv('PERSONAL_DATA_DB_HOST')
    data = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(user=user, password=password,
                                   host=host, database=data)
