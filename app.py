from flask import Flask, jsonify, request
from flask_restful import Resource, Api

#Create flask app
app = Flask(__name__)
#Create API Object
api = Api(app)

