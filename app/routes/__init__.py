from app.routes.users import users_bp
from app.routes.accounts import accounts_bp
from app.routes.pages import pages_bp


def register_routes(app):
    app.register_blueprint(pages_bp)

    app.register_blueprint(
        users_bp,
        url_prefix="/api/users"
    )

    app.register_blueprint(
        accounts_bp,
        url_prefix="/api/accounts"
    )