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
        if not path or not excluded_paths:
            return True

        path += '/' if path[-1] != '/' else ''
        wildcard = any(p.endswith("*") for p in excluded_paths)

        if not wildcard:
            if path in excluded_paths:
                return False

        for p in excluded_paths:
            if p[-1] == '*':
                if path.startswith(p[:-1]):
                    return False
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
