from server.extensions import db
from server.app import create_app
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from werkzeug.security import generate_password_hash


app = create_app()


with app.app_context():
    print(" Creating all tables...")
    db.create_all()


    print("Seeding data...")


    #  Users
    user1 = User(username="admin", password_hash=generate_password_hash("admin123"))
    user2 = User(username="john_doe", password_hash=generate_password_hash("password"))
    db.session.add_all([user1, user2])

    #  Guests
    guest1 = Guest(name="Taylor Swift", occupation="Musician")
    guest2 = Guest(name="Chris Evans", occupation="Actor")
    guest3 = Guest(name="Serena Williams", occupation="Athlete")
    db.session.add_all([guest1, guest2, guest3])

    #  Episodes
    episode1 = Episode(date="2025-06-01", number=101)
    episode2 = Episode(date="2025-06-08", number=102)
    db.session.add_all([episode1, episode2])

    #  Appearances
    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=4, guest=guest2, episode=episode1)
    appearance3 = Appearance(rating=3, guest=guest3, episode=episode2)
    db.session.add_all([appearance1, appearance2, appearance3])

    db.session.commit()
    print("Done seeding!")
