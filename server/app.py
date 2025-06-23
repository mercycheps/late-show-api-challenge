from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from server.controllers import auth_bp, episode_bp, guest_bp, appearance_bp
from server.config import SQLALCHEMY_DATABASE_URI
from server.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object("server.config")

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    JWTManager(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(appearance_bp)

    
    @app.route('/')
    def index():
        return '<h1>a Flask REST API for a Late Night TV show system from scratch</h1>'
    
    return app
