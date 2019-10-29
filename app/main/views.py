from flask import render_template, request, redirect, url_for, abort
from . import main


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to the best  Online Library'
    
    return render_template('index.html', title=title)
