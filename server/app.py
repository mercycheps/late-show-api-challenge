from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from server.controllers.auth_controller import auth_bp
from server.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object("server.config")

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    jwt = JWTManager(app)
    
    app.register_blueprint(auth_bp)
    
    @app.route('/')
    def index():
        return '<h1>a Flask REST API for a Late Night TV show system from scratch</h1>'
    
    return app
