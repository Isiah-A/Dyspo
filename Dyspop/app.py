from flask import Flask
from models import db, User
from os import path
from routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #Initialize the extension with the app
    db.init_app(app)

    #Register all routes
    init_routes(app)


    #Create database if it doesn't exist
    if not path.exists('database.db'):
        with app.app_context():
            db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)







