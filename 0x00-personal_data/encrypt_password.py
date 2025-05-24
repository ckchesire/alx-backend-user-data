#!/usr/bin/env python3
"""
Module for encrypting passwords.
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    Function to hash password with a randomly generated salt.

    Args:
        password (str): The password to be hashed.


    Returns:
        bytes: The salted, hashed password
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password to perform comparison.
        password (str): The plain text password to validate.

    Returns:
        bool: Returns True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
