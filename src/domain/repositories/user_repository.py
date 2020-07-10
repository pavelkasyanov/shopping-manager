import uuid

from src.domain import Session
from src.domain.exceptions.user_exceptions import UserNotFound
from src.domain.models.users import User


class UserRepository:
    def __init__(self):
        self.session = Session()

    def get_all(self):
        return self.session.query(User).all()

    def get_by_login(self, login):
        return self.session.query(User).filter_by(login=login).first()

    @staticmethod
    def create(user: User):
        session = Session()
        user.id = uuid.uuid4()
        session.add(user)
        session.commit()
        return user

    def change_password(self, login, new_password):
        user = self.get_by_login(login)
        if user is None:
            raise UserNotFound(login)
        session = Session()
        user.password = new_password
        current = session.merge(user)
        session.commit()
        return True

    @staticmethod
    def delete(id):
        session = Session()
        current = session.query(User).filter_by(id=id).first()
        session.delete(current)
        session.commit()