from app.extensions import db

class Account(db.Model):
    __tablename__ = "accounts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    account_number = db.Column(db.String(20), unique=True)
    balance = db.Column(db.Numeric(12, 2), default=0)
    currency = db.Column(db.String(3), default="USD")

    user = db.relationship("User", back_populates="accounts")