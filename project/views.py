from flask import Blueprint, current_app

bp = Blueprint("views", __name__)


@bp.route("/")
def index():
    current_app.logger.warning("Hello, welcome to flask!")
    return "Hello, welcome to flask!"
