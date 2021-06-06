"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


DEFAULT_IMG_URL = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/220px-User_icon_2.svg.png'


class User(db.Model):

    def __repr__(self):
        """Show info about users"""
        u = self
        return f'<User id={u.id} first_name={u.first_name} last_name={u.last_name} img_url={u.img_url}>'

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(50), nullable=False, unique=True)

    last_name = db.Column(db.String(50), nullable=False)

    img_url = db.Column(db.String, nullable=False,
                        default=DEFAULT_IMG_URL)

    posts = db.relationship('Post', backref='user',
                            cascade="all,delete-orphan", passive_deletes=True)


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.Text, nullable=False)

    content = db.Column(db.Text)

    created_at = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete="CASCADE"))

    # posts = db.relationship('PostTag', backref='post')
    # posts = db.relationship('Tag', secondary='posts_tags',
    #                         cascade="all,delete", backref='posts')


class PostTag(db.Model):

    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), primary_key=True)

    tag_id = db.Column(db.Integer, db.ForeignKey(
        'tags.id'), primary_key=True)


class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    # posts = db.relationship('PostTag', backref='tags')

    posts = db.relationship('Post', secondary='posts_tags',
                            cascade="all,delete", backref='tags')
