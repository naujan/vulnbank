
from flask import Flask

from app.config import Config
from app.extensions import db


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Import models
    from app import models

    from app.routes.users import users_bp
    app.register_blueprint(
        users_bp,
        url_prefix="/api/users"
    )

    from app.routes.pages import pages_bp
    app.register_blueprint(pages_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
