"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connectdb(app):
    db.app = app
    db.init_app(app)


class User(db.Model):

    __tablename__ = 'users'
