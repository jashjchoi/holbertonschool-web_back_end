#!/usr/bin/env python3
"""new Flask view that handles all routes
for the Session authentication"""
from os import getenv
from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /auth_session/login
    Return:Logged in user
    """
    user_email = request.form.get('email')
    user_pwd = request.form.get('password')
    if not user_email:
        return jsonify({"error": "email missing"}), 400
    if not user_pwd:
        return jsonify({"error": "password missing"}), 400
    try:
        user_results = User.search({'email': user_email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not user_results:
        return jsonify({"error": "no user found for this email"}), 404

    for user in user_results:
        if not user.is_valid_password(user_pwd):
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    user = user_results[0]
    session_id = auth.create_session(user.id)
    SESSION_NAME = getenv("SESSION_NAME")
    res = jsonify(user.to_json())
    res.set_cookie(SESSION_NAME, session_id)
    return res


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ DELETE /auth_session/logout
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
