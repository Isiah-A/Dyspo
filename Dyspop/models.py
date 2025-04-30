import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(50), unique = True, nullable = False)
#     password_hash = db.Column(db.Text)
#     email = db.Column(db.String(120), unique=True, nullable = False)
    # mood_list = db.relationship("MoodEntry", backref = "user")

    # def __init__(self, email, username, password):
    #     self.email = email
    #     self.username = username
    #     self.set_password(password)
    #
    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)
    #
    #
    # def __repr__(self):
    #     return f"<User {self.username}>" #repr is for returning a string
    #     # containing a printable representation of an object which makes debugging better
    #
    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "username": self.username,
    #         "email": self.email
    #     }
    #
    #


class MoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    timestamp = db.Column(db.DateTime, default = datetime.datetime.now, nullable = False)
    name = db.Column(db.String(25), unique = False, nullable = False)
    rating = db.Column(db.Integer, nullable = False)
    notes = db.Column(db.String(100), nullable = True)

    def __repr__(self):
        return f"<MoodEntry {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            # "user_id": self.user_id,
            "timestamp": self.timestamp,
            "name": self.name,
            "rating": self.rating,
            "notes": self.notes
        }
