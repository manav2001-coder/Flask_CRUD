from ..db import db
from sqlalchemy.sql import func

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer,primary_key=True)
    firstName = db.Column(db.String(100),nullable=False)
    lastName = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(500),unique=True,nullable=False)
    password = db.Column(db.String(500),nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())

    def __repr__(self):
        return f"User {self.id} : {self.email}"

class Funds(db.Model):
    __tablename__ = "Funds"
    id = db.Column(db.Integer,primary_key=True)
    amount = db.Column(db.Numeric(10,2),nullable=False)