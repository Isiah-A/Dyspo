from flask import Flask, jsonify, request
from flask_login import LoginManager
from flask_restful import Resource, Api
from Dyspop import create_app
from flask_socketio import SocketIO



app = create_app()
socketio = SocketIO(app)
#Create API Object
api = Api(app)

app.config['SITE_Name'] = 'Dyspo'
app.config['FLASK_DEBUG'] = 1


if __name__ == '__main__':
    socketio.run(app, port=5555, debug = True)

class Dyspo:
    def __init__(self, id, username, email, password, mood_list, user_id, timestamp, mood_name, mood_rating, notes):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.mood_list = mood_list
        self.user_id = user_id
        self.timestamp = timestamp
        self.mood_name = mood_name
        self.mood_rating = mood_rating
        self.notes = notes

    @property
    def get_id(self):
        return self.id





