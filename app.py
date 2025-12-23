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

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

