#!/usr/bin/env python3
"""Module that implements Basic Authentication scheme.
"""
from api.v1.auth.auth import Auth
import base64


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
