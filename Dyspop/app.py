from flask import Flask
from flask_login import LoginManager
from models import db, MoodEntry
from os import path
from routes import init_routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'isiah'
    # login_manager = LoginManager()
    # login_manager.init_app(app)

    #Initialize the extension with the app
    db.init_app(app)

    # @login_manager.user_loader
    # def load_user(userid):
    #     return User.query.get(int(userid))

    #Register all routes
    init_routes(app)

    CORS(app, resources={r"/*": {"origins": "http://localhost:9000"}})

    #Create database if it doesn't exist
    if not path.exists('database.db'):
        with app.app_context():
            db.create_all()

    return app


def pop_db():
    with app.app_context():
        if MoodEntry.query.count() == 0:
            make_entry = MoodEntry.__table__.insert().values([
                { 'id': 1, 'name': 'happy', 'rating': 4, 'notes': 'I laughed today so thats good.'},
                { 'id': 2, 'name': 'sad', 'rating': 1, 'notes': 'Well, thats not gonna go away anytime soon.'},
                { 'id': 3, 'name': 'annoyed', 'rating': 10, 'notes': 'If I think about something long enough I get annoyed.'},
                { 'id': 4, 'name': 'excited', 'rating': 7, 'notes': 'Im gonna work on some sql stuff today, maybe...'}
            ])
            # make_entry = MoodEntry.__table__.insert().values([
            #     {'id': 1, 'name': 'happy', 'rating': 4},
            #     {'id': 2, 'name': 'sad', 'rating': 1 },
            #     {'id': 3, 'name': 'annoyed', 'rating': 10},
            #     {'id': 4, 'name': 'excited', 'rating': 7}
            # ])
            db.session.execute(make_entry)
            db.session.commit()
            print("Database has been populated.")
        else:
            print("Database is already populated.")

if __name__ == '__main__':
    app = create_app()
    pop_db()
    app.run(port=8080 ,debug=True)







