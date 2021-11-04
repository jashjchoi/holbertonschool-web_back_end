#!/usr/bin/env python3
""" Auth module
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth that inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if (
            not authorization_header or type(authorization_header) != str or
            "Basic " not in authorization_header
        ):
            return None
        return authorization_header.split()[1]
