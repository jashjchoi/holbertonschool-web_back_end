#!/usr/bin/env python3
"""Auth class to manage the API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth public method
        that returns False - path
        Improve def require_auth(self, path, excluded_paths)
        by allowing * at the end of excluded paths.
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """public method authorization_header
        that returns None - request will be the Flask request obj
        """
        if request:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """curent_user that returns None - request will be the
        Flask request obj
        """
        return None
