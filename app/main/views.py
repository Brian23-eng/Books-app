from flask import render_template, request, redirect, url_for, abort
from . import main
from ..request import get_books
from .forms import CommentForm
from ..models import Comment, User
from flask_login import login_required


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

