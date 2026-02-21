import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from markupsafe import escape

load_dotenv()
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def hello():
    default_username = os.getenv("DEFAULT_USERNAME")
    name = request.args.get("name", default_username)
    return f"Hello {escape(name)}!"

@app.route("/user")
def hello_username():
    default_username = os.getenv("DEFAULT_USERNAME")
    admin_email = os.getenv("ADMIN_EMAIL")
    return f"<p>Hello, {default_username}, your email is {admin_email}</p>"

@app.route("/health")
def health_check():
    app_version = os.getenv("APP_VERSION")
    
    return jsonify({
        "status": "ok",
        "service": "uplaod-service",
        "version": app_version
        }), 200 


