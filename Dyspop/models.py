from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(80), unique = True)
    password_hash = db.Column(db.Text, nullable = False)
    mood_list = db.relationship("MoodEntry", backref = "user")


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class MoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    timestamp = db.Column(db.DateTime, default = datetime.datetime.now, nullable = False)
    mood_name = db.Column(db.String(25), unique = False, nullable = False)
    mood_rating = db.Column(db.Integer, nullable = False)
    notes = db.Column(db.String(100), nullable = True)