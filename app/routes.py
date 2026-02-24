from flask import Blueprint, jsonify

bp = Blueprint("routes", __name__)

@bp.route("/")
def home():
    return "Hello, world!", 200

@bp.route("/v1/uploads", methods=["POST"])
def upload():
    bp.logger.info("POST to upload an object")
    return jsonify({
        "message": "Not implemented yet",
    }), 501

@bp.route("/v1/health")
def health():
    bp.logger.info("Get /health called")
    return jsonify({
        "status": "ok",
        "service": "upload-service",
        "version": os.getenv("APP_VERSION", "1.0.0")
    }), 200
