#!/usr/bin/env python3
"""Module to perfom session authentication.
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """Implements session authentication.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Method that creates a Session ID for a given user_id. And stores the
        Session ID in the class dictionary.

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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Method returns a user_id based on session id.

        Args:
           session_id (str): a particular session id.

        Returns:
            strs: returns a user id if successfull, else None.
        """
        if session_id is None:
            return None

        if not isinstance(session_id, str):
            return None

        user_id = self.__class__.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        """
        Method returns a user based on a cookie value.

        Args:
           request: http request.

        Return:
           returns the user id.
        """
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Deletes the user session(logout) by removing the session id.

        Args:
           request: Flask request object.

        Returns:
           True if the session was deleted successfully, otherwise False.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
