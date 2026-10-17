from flask import Blueprint, jsonify
from app.extensions import db
from app.models import Account

accounts_bp = Blueprint("accounts", __name__)


@accounts_bp.route("/", methods=["GET"])
def get_accounts():
    accounts = db.session.execute(
        db.select(Account)
    ).scalars().all()

    return jsonify([
        {
            "id": account.id,
            "user_id": account.user_id,
            "account_number": account.account_number,
            "balance": str(account.balance),
            "currency": account.currency
        }
        for account in accounts
    ])


@accounts_bp.route("/<int:account_id>", methods=["GET"])
def get_account(account_id):
    account = db.get_or_404(Account, account_id)

    return jsonify({
        "id": account.id,
        "user_id": account.user_id,
        "account_number": account.account_number,
        "balance": str(account.balance),
        "currency": account.currency
    })
