#!/usr/bin/env python3

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password with bcrypt and return the hash as bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
