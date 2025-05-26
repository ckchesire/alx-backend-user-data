#!/usr/bin/env python3
"""Module to manage the API authentication
"""
from flask import request
from typing import TypeVar, List


class Auth():
    """Class to manage the API Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """No authentication required
        """
        return False

    def authorization_header(self, request=None) -> str:
        """No authentication header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to be updated to retrieve current user details
        """
        return None
