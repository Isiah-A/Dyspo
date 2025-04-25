# Get all users
curl http://127.0.0.1:5000/users

# Create a user
curl -X POST -H "Content-Type: application/json" -d '{"username":"john","email":"john@example.com", "password":"password123"}' http://127.0.0.1:8080/users

# Get a specific user
curl http://127.0.0.1:5000/users/1

# Update a user
curl -X PUT -H "Content-Type: application/json" -d '{"email":"john.updated@example.com"}' http://127.0.0.1:5000/users/1

#Define a file to store cookies
COOKIE_FILE="cookie.txt"

# Login with the created user
# Use the credentials from the 'Create a user' step
echo "Attempting login..."
curl -X POST \
     -d "username=john&password=password123" \
     -c $COOKIE_FILE \
     http://127.0.0.1:8080/login


# Create a mood *using the saved login session*
echo "Attempting to create mood..."
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"mood_name":"Tried","mood_rating":7, "notes":"Need more sleep."}' \
     -b $COOKIE_FILE \
     http://127.0.0.1:5000/moods

# Get the logged-in user's moods *using the saved login session*
echo "Attempting to get user's moods..."
curl -X GET \
     -b $COOKIE_FILE \
     http://127.0.0.1:8080/moods

echo "Attempting to delete mood"
curl -X DELETE \
     -b $COOKIE_FILE \
     http://127.0.0.1:5000/moods/1

# Logout the user *using the saved login session*
echo "Attempting logout..."
curl -X POST \
     -b $COOKIE_FILE \
     http://127.0.0.1:5000/logout


#remove cookie file
rm $COOKIE_FILE

# Delete a user
curl -X DELETE http://127.0.0.1:5000/users/1