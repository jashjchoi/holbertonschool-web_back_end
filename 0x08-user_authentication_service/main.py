#!/usr/bin/env python3
"""Main Module to query your web server for
the corresponding end-point
"""
from app import AUTH
import requests

BASE_URL = 'http://localhost:5000'
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """testing /users
    """
    data = {'email': email, 'password': password}
    response = requests.post(f"{BASEURL}/users", data=data)
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'user created'}


def log_in_wrong_password(email: str, password: str) -> None:
    """testing /sessions
    """
    data = {'email': email, 'password': password}
    response = requests.post(f"{BASEURL}/sessions", data=data)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """testing /sessions
    """
    data = {'email': email, 'password': password}
    response = requests.post(f"{BASEURL}/sessions", data=data)
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'logged in'}
    return response.cookies.get('session_id')


def profile_unlogged() -> None:
    """testing GET /profile
    """
    cookies = {'session_id': None}
    response = requests.get(f"{BASEURL}/profile", cookies=cookies)
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """testing GET /profile
    """
    cookies = {'session_id': session_id}
    response = requests.get(f"{BASEURL}/profile", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {'email': EMAIL}


def log_out(session_id: str) -> None:
    """testing DELETE /sessions
    """
    cookies = {'session_id': session_id}
    response = requests.delete(f"{BASEURL}/sessions", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {'message': 'Bienvenue'}


def reset_password_token(email: str) -> str:
    """testing POST /reset_password
    """
    data = {'email': email}
    response = requests.post(f"{BASEURL}/reset_password", data=data)
    assert response.status_code == 200
    payload = response.json()
    reset_token = payload.get('reset_token')
    assert payload == {'email': email, 'reset_token': reset_token}
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """testing PUT /reset_password
    """
    data = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    }
    response = requests.put(f"{BASEURL}/reset_password", data=data)
    assert response.json() == {'email': email, 'message': 'Password updated'}
    assert response.status_code == 200


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
