# server/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from server.controllers.auth_controller import auth_bp
from flask_jwt_extended import JWTManager

jwt = JWTManager()
jwt.init_app(app)

from .config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy()
migrate = Migrate()
app.register_blueprint(auth_bp)
def create_app():
    app = Flask(__name__)
    app.config.from_object("server.config")

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so Alembic can detect them
    from server import models

    

    return app
