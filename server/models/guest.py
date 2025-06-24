from server.extensions import db

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    appearances = db.relationship("Appearance", backref="guest", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation,
            "appearances": [appearance.id for appearance in self.appearances]  # or include more details if needed
        }
