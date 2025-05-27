#!/usr/bin/env python3
"""Module that implements Basic Authentication scheme.
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Implements Basic Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts Base64 part of the Authorization header for Basic
        Authentication.

        Args:
            authorization_header (str): Value of the Authorization header.

        Returns:
            str: returns the Base64 part of the header, or None if failed.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        Decodes the value of a Base64 string.

        Args:
            base64_authorization_header: base64 encoded string to be decoded

        Returns:
            str: returns the decoded UTF-8 string value of a Base64 string, or
            None on failure.
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_auth = base64.b64decode(base64_authorization_header)
            return decoded_auth.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decode_base64_authorization_header: str) -> (str, str):
        """
        Extracts credentials i.e email and password from the decoded base64
        authroization header.

        Args:
           decode_base64_authorization_header (str): decoded authorization
           string

        Returns:
           Tuple[str, str]: returns a tuple containing user email and password
           or (None, None) on failure.
        """
        if decode_base64_authorization_header is None:
            return None, None

        if not isinstance(decode_base64_authorization_header, str):
            return None, None

        if ':' not in decode_base64_authorization_header:
            return None, None

        email, password = decode_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Method to return User instance based on email and password.

        Args:
           user_email (str): a particular user email
           user_pwd (str): a particular user password

        Return:
            User: returns the User instance based on their email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
        except Exception:
            return None

        if not users or len(users) == 0:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user
