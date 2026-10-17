from app.extensions import db
from datetime import datetime, timezone

class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    from_account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"))
    to_account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"))
    amount = db.Column(db.Numeric(12, 2))
    description = db.Column(db.Text)
    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    sender = db.relationship("Account", foreign_keys=[from_account_id])
    receiver = db.relationship("Account", foreign_keys=[to_account_id])