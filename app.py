from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake database
users = []

@app.route("/")
def home():
    return "User Management System is running"

@app.route("/add-user", methods=["POST"])
def add_user():
    data = request.json

    user = {
        "username": data["username"],
        "role": data["role"]
    }

    users.append(user)
    return jsonify({"message": "User added successfully"})

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
