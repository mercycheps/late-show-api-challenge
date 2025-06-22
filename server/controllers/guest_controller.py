import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret")


from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    current_user = get_jwt_identity()
    ...
