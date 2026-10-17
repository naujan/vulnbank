
from app.extensions import db
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(255))
    role = db.Column(db.String(20), default="user")
    full_name = db.Column(db.String(100))

    accounts = db.relationship("Account", back_populates="user")
    messages = db.relationship("Message", back_populates="user")
    sessions = db.relationship("Session", back_populates="user")
