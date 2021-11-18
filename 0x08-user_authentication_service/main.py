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
    """ Testing register_user
    """
    data = {"email": email, "password": password}
    response = requests.post("http://localhost:5000/users", data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """ Testing log_in_wrong_password
    """
    data = {"email": email, "password": password}
    response = requests.post("http://0.0.0.0:5000/sessions", data)
    assert response.status_code == 401


def profile_unlogged() -> None:
    """ Testing profile_unlogged
    """
    response = requests.get("http://0.0.0.0:5000/profile")
    assert response.status_code == 403


def log_in(email: str, password: str) -> str:
    """ Testing log_in
    """
    data = {"email": email, "password": password}
    response = requests.post("http://0.0.0.0:5000/sessions", data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}
    return response.cookies.get("session_id")


def profile_logged(session_id: str) -> None:
    """ Testing profile_logged
    """
    found_user = AUTH.get_user_from_session_id(session_id)
    cookies = {"session_id": session_id}
    response = requests.get("http://0.0.0.0:5000/profile", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {"email": found_user.email}


def log_out(session_id: str) -> None:
    """ Testing log_out
    """
    cookies = {"session_id": session_id}
    response = requests.delete("http://0.0.0.0:5000/sessions", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """ Testing reset_password_token
    """
    data = {"email": email}
    response = requests.post("http://0.0.0.0:5000/reset_password", data)
    found_user = AUTH._db.find_user_by(email=email)
    res_tok = found_user.reset_token
    assert response.status_code == 200
    assert response.json() == {"email": email, "reset_token": res_tok}
    return res_tok


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Testing update_password
    """
    data = {"email": email, "reset_token": reset_token,
            "new_password": new_password}
    response = requests.put("http://0.0.0.0:5000/reset_password", data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


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
