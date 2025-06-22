from flask import Flask
from flask_cors import CORS
from server.controllers.auth_controller import auth_bp

from server.extensions import db, migrate
from server.config import SQLALCHEMY_DATABASE_URI

def create_app():
    app = Flask(__name__)
    app.config.from_object("server.config")

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    app.register_blueprint(auth_bp)
    return app
