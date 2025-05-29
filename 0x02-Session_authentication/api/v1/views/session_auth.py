#!/usr/bin/env python3
"""Module for session authentication.
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from api.v1.app import auth
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """
    POST /api/v1/auth_session/login
    route handles session authentication.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None:
        return jsonify({"error": "email missing"}), 400

    if password is None:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({"email": email})
    except Exception:
        return None

    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())
    cookie_name = os.getenv("SESSION_NAME")
    response.set_cookie(cookie_name, session_id)

    return response


@app_views.route(
        '/auth_session/logout',
        methods=['DELETE'],
        strict_slashes=False)
def logout():
    """
    Handle DELETE request to log out a user by destroying their session.
    """
    if not auth.destroy_session(request):
        abort(404)

    return jsonify({}), 200
