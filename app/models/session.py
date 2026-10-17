from app.extensions import db

class Session(db.Model):
    __tablename__ = "sessions"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    session_token = db.Column(db.String(255), unique=True)
    expires_at = db.Column(db.DateTime)

    user = db.relationship("User", back_populates="sessions")
