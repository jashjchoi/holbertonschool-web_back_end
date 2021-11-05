#!/usr/bin/env python3
""" Auth module
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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

    def decode_base64_authorization_header(self,
                                           authorization_header: str) -> str:
        """returns the decoded value of a Base64 string
        base64_authorization_header
        """
        if not authorization_header or \
           not isinstance(authorization_header, str):
            return None
        try:
            b = base64.b64decode(authorization_header)
            decoded_code = b.decode("utf-8")
        except Exception:
            return None
        return decoded_code

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """returns the user email and password from the Base64 decoded value
        """
        if (
            not decoded_base64_authorization_header or
            type(decoded_base64_authorization_header) != str or
            ':' not in decoded_base64_authorization_header
        ):
            return None, None
        sep = decoded_base64_authorization_header.find(":")
        user = decoded_base64_authorization_header[:sep]
        pwd = decoded_base64_authorization_header[sep + 1:]
        return user, pwd

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password
        """
        if (
            not user_email or type(user_email) != str or not
            user_pwd or type(user_pwd) != str
        ):
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None
        if user:
            for u in user:
                if u.is_valid_password(user_pwd):
                    return u
        return None
