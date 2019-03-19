import logging
import os

from flask import Flask
from werkzeug.utils import find_modules, import_string

from .ext import db


def create_app(**kwargs):
    app = Flask(__name__)
    app.config.from_object("config")
    app.config.from_mapping(**kwargs)

    db.init_app(app)

    setup_logger(app)
    setup_blueprints(app)

    return app


def setup_logger(app):
    filename = app.config.get("LOGGER_FILENAME")
    formatter = app.config.get("LOGGER_FORMATTER", "[%(asctime)s] %(funcName)s:%(lineno)d %(levelname)s %(message)s")
    level = app.config.get("LOGGER_LEVEL", logging.INFO)

    if not filename:
        from flask.logging import default_handler

        handler = default_handler
    else:
        filename = os.path.abspath(filename)
        folder = os.path.dirname(filename)
        if not os.path.exists(folder):
            os.makedirs(folder)

        handler = logging.FileHandler(filename, encoding="utf-8")

    handler.setFormatter(logging.Formatter(formatter))
    handler.setLevel(level)
    app.logger.addHandler(handler)


def setup_blueprints(app):
    for name in find_modules(__name__, recursive=True):
        obj = import_string(name)
        if hasattr(obj, "bp"):
            bp = getattr(obj, "bp")
            app.register_blueprint(bp)
