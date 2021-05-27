"""Blogly application."""

from flask import Flask
from flask.templating import render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/blogly?user=postgres&password=postgresql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'flaskblogly'

connect_db(app)


@app.route('/')
def home_page():
    """"list all users"""
    users = User.query.all()
    return render_template('user.html', users=users)


@app.route('/<int:user_id>')
def detail_page(user_id):
    """show user details"""

    user = User.query.get_or_404(user_id)
    return render_template('details.html', user=user)
