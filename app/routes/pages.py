from flask import Blueprint, render_template

pages_bp = Blueprint("pages", __name__)


@pages_bp.route("/")
def home():
    return render_template("index.html")
@pages_bp.route("/account")
def account():
    return render_template("account.html")
@pages_bp.route("/about")
def about():
    return render_template("about.html")
@pages_bp.route("/contact")
def contact():
    return render_template("contact.html")