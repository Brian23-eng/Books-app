from flask import render_template, request, redirect, url_for, abort, current_app, flash
from PIL import Image
from . import main
from ..import db
from ..request import get_books,get_book
from .forms import CommentForm, UpdateAccountForm
from ..models import Comment, User, Books, Preview
from flask_login import login_required, current_user
import os
import secrets




@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    book = get_books()
    title = 'Home - Welcome to the best  Online Library'
    
    
    return render_template('index.html', title=title, book=book)

@main.route('/comments/<book_rank>')

@login_required

def comments(book_rank):

    book = Book.query.filter_by(rank = book_rank).first()

    comments = Comment.query.filter_by(book_rank = book.rank).order_by(Comment.posted.desc())

    return render_template('comments.html', book = book, comments = comments)


@main.route('/book/comment/new/<book_rank>', methods = ['GET', 'POST'])

@login_required

def new_comment(book_rank):

    form = CommentForm()

    book = Book.query.filter_by(rank = book_rank).first()

    comment = Comment()

    if form.validate_on_submit():

        comment.title = form.title.data

        comment.comment = form.comment.data

        comment.book_rank = book_rank

        comment.user_id = current_user.id


        db.session.add(comment)

        db.session.commit()

        return redirect(url_for('main.comments', book_rank = book_rank ))

    return render_template('new_comment.html', comment_form = form)


@main.route("/review/")
@login_required
def review():
    preview = get_book()

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Preview - Welcome to the best  Online Library'
    # preview = Preview.query.filter_by(book_rank = rank).all()
    
    
    if current_user.is_authenticated:
        return redirect(url_for('main.review'))
    book = Books(rank, title, author, poster, description, publisher)
    return render_template('review.html',rank=rank, title=title, preview=preview, review=review)

@main.route("/account", methods=['GET', 'POST'])
def account():
    form = UpdateAccountForm()
    
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
            
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been activated!', 'success')
        return redirect(url_for('main.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        
    image_file = url_for('static', filename='photos' + current_user.image_file)
    
    return render_template('account.html', title='Account | Welcome to Online Library',form=form)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/photos', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn





