import socketio
from flask import Flask
from Dyspop.routes import rt


def create_app():
    app = Flask(__name__, instance_relative_config = False)
    app.config.from_object('config.Config')
    app.register_blueprint(rt)
    from Dyspop.models import db
    db.init_app(app)

    with app.app_context():
        db.create_all()
        return app