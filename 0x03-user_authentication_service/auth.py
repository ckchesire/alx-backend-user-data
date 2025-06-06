#!/usr/bin/env python3
"""Auth module"""

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Optional, Union


def _hash_password(password: str) -> bytes:
    """
    Hash a password with bcrypt and return the hash as bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Generates a new UUID and return its string representation.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user if they do not exist.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email=email,
                                     hashed_password=hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Lookup user email and validate user password.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(password.encode(),
                                       user.hashed_password):
                return True
            return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> Optional[str]:
        """
        Create a session ID for the user with the given email.
        Store the session ID in the DB and return it.
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str):
        """
        Method to retrieve a user by their session_id
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except Exception:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """
        Destroys the session (logs out a user) by setting session_id to None
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception as e:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a reset token for a user by email
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            raise ValueError("User does not exist")

        reset_token = str(uuid.uuid4())
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token
