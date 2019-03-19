from datetime import datetime

from .ext import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(256), nullable=False, default="")
    text = db.Column(db.Text, nullable=False, default="")
    state = db.Column(db.SmallInteger, nullable=False, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
