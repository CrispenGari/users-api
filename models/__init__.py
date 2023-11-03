from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    gender = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(120), nullable=False)

    def __init__(self, name: str, email: str, gender: str, surname: str):
        self.name = name
        self.surname = surname
        self.email = email
        self.gender = gender

    def json(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "gender": self.gender,
            "id": self.id,
        }

    def __repr__(self):
        return "<User %r>" % self.name

    def __str__(self):
        return "<User %r>" % self.name
