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


@main.route('/book/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    book = get_book(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(book_rank = book_rank,
                            movie_title = book.title,
                            image_path = book.poster,
                            review_title = title,
                            book_review = review,
                            user = current_user)
        new_review.save_review()
        return redirect(url_for('main.book',id = book_rank ))

    title = f'{movie.title} review'
    return render_template('new_review.html',
                            title = title, 
                            review_form = form, 
                            book = book)

@main.route("/review/<int:id>")
def single_review(id):
    review = Review.query.get(id)

    if review is None:
        abort(404)
    format_review_title = markdown2.markdown(review.review_title,
                                            extras = ["code-friendly", "fenced-code-blocks"])
    format_review = markdown2.markdown(review.movie_review,
                                        extras = ["code-friendly", "fenced-code-blocks"])
    
    return render_template("review.html", 
                            review = review,
                            format_review_title = format_review_title,
                            format_review = format_review)
