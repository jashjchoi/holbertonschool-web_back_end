#!/usr/bin/env python3
"""SessionExpAuth add an expiration date to a Session ID
"""
from os import getenv
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from models.user import User


class SessionExpAuth(SessionAuth):
    """inherits from SessionAuth
    """
    def __init__(self):
        """Initialize instance attribute session_duration
        """
        try:
            self.session_duration = int(getenv('SESSION_DURATION', 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create new Session ID
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        SessionExpAuth.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Return user_id from the session dictionary
        """
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None
        if self.session_duration <= 0:
            return session_dict.get('user_id')

        created_at = session_dict.get('created_at')
        if created_at is None:
            return None
        expired_t = created_at + timedelta(seconds=self.session_duration)
        if expired_t < datetime.now():
            return None
        return session_dict.get('user_id')
