from flask import Blueprint, request, jsonify
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.extensions import db
from flask_jwt_extended import jwt_required


episode_bp = Blueprint("episodes", __name__, url_prefix="/episodes")


@episode_bp.route("/", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200



@episode_bp.route("/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return {"error": "Episode not found"}, 404


    appearances = Appearance.query.filter_by(episode_id=episode.id).all()
    return {
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [a.to_dict() for a in appearances],
    }, 200


@episode_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return {"error": "Episode not found"}, 404
    

    db.session.delete(episode)
    db.session.commit()
    return {"message": "Episode and associated appearances deleted"}, 200
