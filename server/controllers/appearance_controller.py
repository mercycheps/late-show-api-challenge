from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server.models.episode import Episode
from server.models.guest import Guest
from server.extensions import db
from flask_jwt_extended import jwt_required


appearance_bp = Blueprint("appearances", __name__, url_prefix="/appearances")


@appearance_bp.route("/", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()


    rating = data.get("rating")
    guest_id = data.get("guest_id")
    episode_id = data.get("episode_id")


    if not all([rating, guest_id, episode_id]):
        return {"error": "rating, guest_id and episode_id required"}, 400

    if not (1 <= rating <= 5):
        return {"error": "Rating must be between 1 and 5"}, 400


    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)

    if not guest or not episode:
        return {"error": "Invalid guest_id or episode_id"}, 404


    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)


    db.session.add(appearance)
    db.session.commit()

    return appearance.to_dict(), 201
