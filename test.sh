# Get all users
curl http://127.0.0.1:5000/users

# Create a user
curl -X POST -H "Content-Type: application/json" -d '{"username":"john","email":"john@example.com", "password":"password123"}' http://127.0.0.1:5000/users

# Get a specific user
curl http://127.0.0.1:5000/users/1

# Update a user
curl -X PUT -H "Content-Type: application/json" -d '{"email":"john.updated@example.com"}' http://127.0.0.1:5000/users/1

# Create a mood
curl -X POST -H "Content-Type: application/json" -d '{"mood_name":"Happy","mood_rating":5, "notes":"Feeling okay because I got this to work in a day."}' http://127.0.0.1:5000/moods

# Delete a user
curl -X DELETE http://127.0.0.1:5000/users/1