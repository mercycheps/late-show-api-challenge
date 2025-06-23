import json
from server.extensions import db
from server.models.user import User
from flask_jwt_extended import create_access_token


def test_register_user(client):
    res = client.post("/register", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert res.status_code == 201
    assert res.get_json()["message"] == "User created successfully"


def test_login_user(client):
    user = User(username="testuser")
    user.set_password("testpass")
    db.session.add(user)
    db.session.commit()

    res = client.post("/login", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert res.status_code == 200
    assert "access_token" in res.get_json()


def test_get_episodes(client):
    res = client.get("/episodes")
    assert res.status_code == 200


def test_get_episode_by_id(client):
    # You need to add an episode before testing
    from server.models.episode import Episode
    episode = Episode(date="2025-01-01", number=1)
    db.session.add(episode)
    db.session.commit()

    res = client.get(f"/episodes/{episode.id}")
    assert res.status_code == 200


def test_delete_episode_auth_required(client):
    from server.models.episode import Episode

    # Add user and episode
    user = User(username="admin")
    user.set_password("adminpass")
    db.session.add(user)

    episode = Episode(date="2025-01-01", number=2)
    db.session.add(episode)
    db.session.commit()

    # Get token
    token = create_access_token(identity=user.id)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    res = client.delete(f"/episodes/{episode.id}", headers=headers)
    assert res.status_code in (200, 204)  # Depending on your route response


def test_get_guests(client):
    res = client.get("/guests")
    assert res.status_code == 200


def test_create_appearance_auth_required(client):
    from server.models.guest import Guest
    from server.models.episode import Episode
    from server.models.user import User

    guest = Guest(name="Guest 1", occupation="Actor")
    episode = Episode(date="2025-01-01", number=3)
    user = User(username="creator")
    user.set_password("password")

    db.session.add_all([guest, episode, user])
    db.session.commit()

    token = create_access_token(identity=user.id)
    headers = {
        "Authorization": f"Bearer {token}"
    }

    res = client.post("/appearances", json={
        "guest_id": guest.id,
        "episode_id": episode.id,
        "rating": 4
    }, headers=headers)

    assert res.status_code == 201
