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







