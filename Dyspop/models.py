import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    # password = db.Column(db.String(100), nullable = False)
    # mood_list = db.relationship("MoodEntry", backref = "user", lazy = True)


    def __repr__(self):
        return f"<User {self.username}>" #repr is for returning a string
        # containing a printable representation of an object which makes debugging better

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }




class MoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    timestamp = db.Column(db.DateTime, default = datetime.datetime.now, nullable = False)
    mood_name = db.Column(db.String(25), unique = False, nullable = False)
    mood_rating = db.Column(db.Integer, nullable = False)
    notes = db.Column(db.String(100), nullable = True)

    def __repr__(self):
        return f"<MoodEntry {self.mood_name}>"
