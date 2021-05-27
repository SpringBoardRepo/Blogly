"""Models for Blogly."""
from enum import unique
from re import U
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


DEFAULT_IMG_URL = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.phpfoxer.com%2Fblog%2Fphpfox-default-avatar&psig=AOvVaw3U-5h03AE38bWKdxjJVzEo&ust=1622237580174000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPi8p4ro6vACFQAAAAAdAAAAABAF'


class User(db.Model):

    def __repr__(self):
        """Show info about users"""
        u = self
        return f'<User id={u.id} first_name={u.first_name} last_name={u.last_name} img_url={u.img_url}>'

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(50), nullable=False, unique=True)

    last_name = db.Column(db.String(50), nullable=False)

    img_url = db.Column(db.String(500), nullable=False,
                        default=DEFAULT_IMG_URL)
