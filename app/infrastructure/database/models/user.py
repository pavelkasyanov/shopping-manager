from app.infrastructure.database.db import db


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String, nullable=False)
    nickname = db.Column(db.Unicode, nullable=False)
    password = db.Column("password", db.String, nullable=False)
    is_banned = db.Column("is_banned", db.Boolean, nullable=True)
    is_superuser = db.Column("is_superuser", db.Boolean, nullable=True)
    created_date = db.Column(
        "created_date", db.DateTime, default=db.func.now(), nullable=False
    )
