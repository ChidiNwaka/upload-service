from flask import Blueprint, jsonify

bp = Blueprint("health", __name__)

@bp.route("/health")
def health_check():

    return jsonify({
        "status": "ok",
        "service": "upload-service",
        }), 200
# Add the version gotten from the .env file above
