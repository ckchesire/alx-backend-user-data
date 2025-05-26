#!/usr/bin/env python3
"""Module to manage the API authentication
"""
from flask import request
from typing import TypeVar, List


class Auth():
    """Class to manage the API Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if authentication is required for a given path.

           Returns:
              - True if path is None
              - True if excluded_paths is None or empty
              - False if path matches (with slash tolerance)
              - False if path in excluded_paths
              - False otherwise
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded_paths == path:
                return False

        return False

    def authorization_header(self, request=None) -> str:
        """No authentication header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to be updated to retrieve current user details
        """
        return None
