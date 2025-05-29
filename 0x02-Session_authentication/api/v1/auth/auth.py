#!/usr/bin/env python3
"""Module to manage the API authentication
"""
from flask import request
from typing import TypeVar, List
import os


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
              - Supports wildcard '*' at the end of excluded paths
              - False otherwise
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded.endswith('*'):
                if path.startswith(excluded[:-1]):
                    return False
            else:
                if not excluded.endswith('/'):
                    excluded += '/'
                if excluded == path:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """No authentication header
        """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None

        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to be updated to retrieve current user details
        """
        return None

    def session_cookie(self, request=None):
        """
        Method to return a cookie value from a request.

        Args:
           request: http request

        Returns:
            returns the session cookie.
        """
        if request is None:
            return None

        session_name = os.getenv("SESSION_NAME")
        if session_name is None:
            return None

        return request.cookies.get(session_name)
