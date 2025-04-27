from flask import request, jsonify, render_template
from flask_login import login_manager, login_required, current_user, login_user, logout_user, LoginManager
from models import db, MoodEntry
#jsonify Serializes the given arguments as JSON

# login_manager = LoginManager()

def init_routes(app):


    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))

    @app.route('/', methods=['GET'])
    def home():
        return "Home Page!"

    # @app.route('/login', methods=['POST'])
    # def login():
    #     #will return None instead of raising an error if using request.form[]
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #
    #     if not username or not password:
    #         return jsonify({'error': 'username and password are required'})

        # user = User.query.filter_by(username=username).first()

        # if user and user.check_password(password):
        #     login_user(user)
        #     return jsonify({"message": "Login successful!", "user": user.to_dict()}), 200
        # else:
        #     return jsonify({'error': 'Invalid username or password'}), 401

    # @app.route('/logout', methods=["POST"])
    # @login_required
    # def logout():
    #     logout_user()
    #     return jsonify({"message": "Logout successful!"}), 200
    #
    # @app.route('/users', methods=['GET'])
    # def get_users():
    #     users = User.query.all()
    #     return jsonify([user.to_dict() for user in users])
    #
    # @app.route('/users/<int:user_id>', methods=['GET'])
    # def get_user(user_id):
    #     user = User.query.get_or_404(user_id)
    #     return jsonify(user.to_dict())
    #
    # @app.route('/users', methods=['POST'])
    # def create_user():
    #     data = request.get_json()
    #     print("data received:", data)
    #     new_user = User(username=data['username'], email=data['email'], password=data['password']) #added password
    #     db.session.add(new_user)
    #     db.session.commit()
    #     return jsonify(new_user.to_dict()), 201
    #
    # @app.route('/users/<int:user_id>', methods=['PUT'])
    # def update_user(user_id):
    #     user = User.query.get_or_404(user_id)
    #     data = request.get_json()
    #
    #     if 'username' in data:
    #         user.username = data['username']
    #     if 'email' in data:
    #         user.email = data['email']
    #     if 'password' in data:
    #         user.set_password(data['password'])
    #
    #     db.session.commit()
    #     return jsonify(user.to_dict())
    #
    # @app.route('/users/<int:user_id>', methods=['DELETE'])
    # def delete_user(user_id):
    #     user = User.query.get_or_404(user_id)
    #     db.session.delete(user)
    #     db.session.commit()
    #     return '', 204

    #Mood Entry Routes
    @app.route('/moods', methods=['POST'])
    # @login_required #need to login to create a mood
    def create_mood():
        data = request.get_json()
        print("Mood received:", data)
        new_mood = MoodEntry(
            # user_id = current_user.id,
            mood_name = data['mood_name'],
            mood_rating = int(data['mood_rating']),
            notes = data.get('notes'))
        db.session.add(new_mood)
        db.session.commit()
        return jsonify(new_mood.to_dict()), 201


    @app.route('/moods', methods = ['GET'])
    # @login_required
    def get_moods():
        #should get moods for currently logged-in user
        moods = MoodEntry.query.all()
        # moods = MoodEntry.query.filter_by(user_id = current_user.id).order_by(MoodEntry.timestamp.desc()).all()
        return jsonify([mood.to_dict() for mood in moods])


    @app.route('/moods/<int:entry_id>', methods = ['GET'])
    # @login_required
    def get_mood_entry(entry_id):
        mood = MoodEntry.query.get_or_404(entry_id)
        return jsonify(mood.to_dict())


    @app.route('/moods/<int:entry_id>', methods = ['GET'])
    # @login_required
    def update_mood(entry_id):
        mood = MoodEntry.query.get_or_404(entry_id)
        data = request.get_json()
        if 'mood_name' in data:
            mood.mood_name = data['mood_name']
        if 'mood_rating' in data:
            mood.mood_rating = int(data['mood_rating'])
        if 'notes' in data:
            mood.notes = data['notes']
        db.session.commit()
        return jsonify(mood.to_dict())


    @app.route('/moods/<int:entry_id>', methods = ['DELETE'])
    # @login_required
    def delete_mood_entry(entry_id):
        mood = MoodEntry.query.get_or_404(entry_id)
        db.session.delete(mood)
        db.session.commit()
        return '', 204

