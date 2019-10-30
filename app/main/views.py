from flask import render_template, request, redirect, url_for, abort
from . import main
from ..request import get_books


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    book = get_books()
    title = 'Home - Welcome to the best  Online Library'
    
    return render_template('index.html', title=title, book=book)
