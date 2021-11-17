#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB class
    """
    def __init__(self):
        """Constructor"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add the new user"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find and returns the first row found in the
        users table as filtered by input"""
        session = self._session
        query = session.query(User).filter_by(**kwargs)
        return query.one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """find_user_by to locate the user"""
        user = self.find_user_by(id=user_id)
        for key in kwargs:
            if key not in user.__dir__():
                raise ValueError
            setattr(user, key, kwargs[key])
        self._session.commit()
        return None
