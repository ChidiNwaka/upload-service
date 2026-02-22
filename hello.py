import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from markupsafe import escape

load_dotenv()
app = Flask(__name__)

users = [
    {
        "userid": "1",
        "username": "john_doe",
        "name": "John Doe",
        "email": "j_doe@example.com",
        "city": "San Francisco",
    },
    {
        "userid": "2",
        "username": "k_fara",
        "name": "Kate Faraday",
        "email": "k_faraday@example.com",
        "city": "Toronto"
    }
]

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route("/users")
def get_users():
    return jsonify(users), 200

@app.route("/users/<string:user_id>", methods=['GET'])
def get_user(user_id: str):
    user_id = escape(user_id)

    found_user = next((user for user in users if user["userid"] == user_id), None)
    
    if not found_user:
        return jsonify({"error": f"User not found with id: {user_id}"}), 404
    return jsonify(found_user), 200

@app.route("/hello")
def hello():
    default_username = os.getenv("DEFAULT_USERNAME")
    name = request.args.get("name", default_username)
    return f"Hello {escape(name)}!", 200

@app.route("/health")
def health_check():
    app_version = os.getenv("APP_VERSION")
    
    return jsonify({
        "status": "ok",
        "service": "uplaod-service",
        "version": app_version
        }), 200 


