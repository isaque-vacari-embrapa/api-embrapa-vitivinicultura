from models.base.database import db
from sqlalchemy import Index


class User(db.Model):
    __bind_key__ = "auth"
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), nullable=False, default="example@mail.com")
    role = db.Column(db.String(32), nullable=False, default="user")

    __table_args__ = (Index("user_username", "username"),)
