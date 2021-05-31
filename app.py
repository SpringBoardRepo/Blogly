"""Blogly application."""

from flask import Flask, request, redirect, flash
from flask.templating import render_template
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/blogly?user=postgres&password=postgresql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'flaskblogly'

connect_db(app)


@app.route('/')
def home_page():
    """"list all users"""
    users = User.query.order_by(User.first_name, User.last_name).all()
    return render_template('user.html', users=users)


@app.route('/<int:user_id>')
def detail_page(user_id):
    """show user details"""
    user = User.query.get_or_404(user_id)
    posts = Post.query.get(user_id)
    return render_template('details.html', user=user, posts=posts)


@app.route('/new')
def new_user():
    """Add a new user"""
    return render_template('new_user.html')


@app.route('/', methods=['POST'])
def add_user():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    img_url = request.form['img-url'] or None

    new_user = User(first_name=first_name,
                    last_name=last_name, img_url=img_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect(f'/{new_user.id}')


@app.route('/<int:user_id>/edit')
def edit_user_form(user_id):
    """Edit user info"""
    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user=user)


@app.route('/<int:user_id>/edit', methods=['POST'])
def edit_user(user_id):
    """Edit user info"""
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first-name']
    user.last_name = request.form['last-name']
    user.img_url = request.form['img-url'] or None

    db.session.add(user)
    db.session.commit()
    return redirect(f'/{user.id}')


@app.route('/<int:user_id>/delete')
def delete_user(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect('/')


#########################################################################################################################
"""Posts routes"""


@app.route('/user/<int:user_id>/add_post')
def add_post(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('add_post.html', user=user)


@app.route('/user/<int:user_id>/add_post', methods=['Post'])
def user_add_post(user_id):
    """Add a user's new post"""
    user = User.query.get_or_404(user_id)
    title = request.form['post-title']
    content = request.form['post-content']
    new_post = Post(title=title, content=content, user_id=user.id)

    db.session.add(new_post)
    # db.session.rollback()
    db.session.commit()
    return redirect(f'/{user.id}')


@app.route('/post/<int:post_id>')
def show_user_post(post_id):
    post = Post.query.get(post_id)
    return render_template('post.html', post=post)


@app.route('/post/<int:post_id>/edit')
def edit_post(post_id):
    """edit user post"""
    post = Post.query.get(post_id)
    return render_template('edit_post.html', post=post)


@app.route('/post/<int:post_id>/edit', methods=['POST'])
def edit_user_post(post_id):
    """Edit user post """
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    db.session.add(post)
    db.session.commit()

    return redirect(f'/{post.id}')


@app.route('/post/<int:post_id>/delete')
def delete_post(post_id):
    """Delete user's post"""
    Post.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect('/')
