from app.database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger(), primary_key=True)
    nickname = db.Column(db.Unicode(), default="unnamed")
    email = db.Column(db.Str())
    is_baned = db.Column(db.Boolean(), default=False)
