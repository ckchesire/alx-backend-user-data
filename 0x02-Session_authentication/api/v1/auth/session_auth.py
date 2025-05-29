#!/usr/bin/env python3
"""Module to perfom session authentication.
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Implements session authentication.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Method that creates a Session ID for a given user_id. And stores the
        Session ID and

        Args:
           user_id (str): a particular user's id.

        Returns:
            str: returns the session id string if successful otherwise None.
        """
        if user_id is None:
            return None

        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.__class__.user_id_by_session_id[session_id] = user_id

        return session_id
