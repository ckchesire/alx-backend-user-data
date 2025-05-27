#!/usr/bin/env python3
"""Module that implements Basic Authentication scheme.
"""
from api.v1.auth.auth import Auth


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
