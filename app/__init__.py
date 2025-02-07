from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="../templates")
    app.config.from_object("config")

    db.init_app(app)

    from app.routes import auth, reservations, admin, general
    app.register_blueprint(auth, url_prefix="/auth")
#    app.register_blueprint(reservations, url_prefix="/reservations")
    #app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(general, url_prefix="/")

    return app
