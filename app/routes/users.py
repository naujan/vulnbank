from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models import User

users_bp = Blueprint("users", __name__)


@users_bp.route("/", methods=["GET"])
def get_users():
    users = db.session.execute(
        db.select(User)
    ).scalars().all()

    return jsonify([
        {
            "id": user.id
        }
        for user in users
    ])


@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = db.get_or_404(User, user_id)

    return jsonify({
        "id": user.id
    })
