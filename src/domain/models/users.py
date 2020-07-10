from alembic import op
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, BYTEA
from sqlalchemy.orm import relationship

from src.domain import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True)
    login = Column(String, unique=True)
    password = Column(BYTEA, unique=False)
    email = Column(String)

    role_id = Column(ForeignKey('user_roles.id', onupdate='CASCADE'), index=True)

    role = relationship('UserRole', primaryjoin='User.role_id == UserRole.id',
                        backref='users')


class UserRole(Base):
    __tablename__ = 'user_roles'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(80), unique=True)


class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True))


class UserSettings(Base):
    __tablename__ = 'user_settings'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True))

    name = Column(String, unique=False)
    surname = Column(String, unique=False)
    patronymic = Column(String, unique=False)