import os
from flask import Flask, request, jsonify, url_for
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
    return "<p>Hello, World!</p>", 200

@app.route("/users")
def get_users():
    app.logger.info("Started the call to get_users")
    app.logger.info("Finished the call to get_users")
    return jsonify(users), 200

@app.route("/users/<string:user_id>", methods=['GET'])
def get_user(user_id: str):
    
    user_id = escape(user_id)
    
    app.logger.info(f"GET /users/{user_id} requested")

    found_user = next((user for user in users if user["userid"] == user_id), None)
    
    if not found_user:
        app.logger.warning(f"User not found: user_id: {user_id}")
        return jsonify({"error": f"User not found with id: {user_id}"}), 404

    app.logger.info(f"User fetched successfully: user_id={user_id}")
    
    return jsonify(found_user), 200

@app.route("/hello")
def hello():
    default_username = os.getenv("DEFAULT_USERNAME")
    name = request.args.get("name", default_username)
    print("request: ", request)
    return f"Hello {escape(name)}!", 200
    
@app.route("/health")
def health_check():
    app_version = os.getenv("APP_VERSION")
    
    return jsonify({
        "status": "ok",
        "service": "upload-service",
        "version": app_version
        }), 200 

with app.test_request_context():
    print(url_for('hello'))
