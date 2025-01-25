from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    from app.routes import auth_bp, reservations_bp, admin_bp, general
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(reservations_bp, url_prefix="/reservations")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(general, url_prefix="/")

    return app
