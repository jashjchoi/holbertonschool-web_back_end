#!/usr/bin/env python3
"""Basic Flask app
"""
from auth import Auth
from flask import Flask, jsonify, request, abort, redirect
from flask.helpers import make_response
from sqlalchemy.orm.exc import NoResultFound

AUTH = Auth()
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/', methods=['GET'], strict_slashes=False)
def hello() -> str:
    """GET route index
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def user() -> str:
    """POST route for user register that implements the POST /users route
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"}), 200
    except Exception:
        return jsonify({"messege": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """login function to respond to the POST /sessions route
    """
    email = request.form.get('email')
    password = request.form.get('password')
    valid_login = AUTH.valid_login(email, password)
    if not valid_login:
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": f"{email}", "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """Logout function
    If the user exists destroy the session and redirect the user to GET /
    If the user does not exist, respond with a 403 HTTP status"""
    session_id = request.cookies.get("session_id")
    if session_id is not None:
        user = AUTH.get_user_from_session_id(session_id)
        if user is not None:
            AUTH.destroy_session(user.id)
            return redirect("/")
    return abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ GET /profile
    Find the user. If the user exist, respond with a 200 HTTP status
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """get_reset_password
    Return:
       str: message
    """
    email = request.form.get('email')
    user = AUTH.create_session(email)
    if not user:
        abort(403)
    else:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": f"{email}", "reset_token": f"{token}"})


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """update password
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_pdw = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, new_pdw)
        return jsonify({"email": f"{email}",
                        "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
