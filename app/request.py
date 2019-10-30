import urllib.request, json
import requests
from .models import Books
# Getting api key
api_key = None
# Getting the book base url
base_url = None
def configure_request(app):
    global api_key, base_url
    api_key = app.config["BOOK_API_KEY"]
    base_url = app.config["BOOK_API_BASE_URL"]
def get_books():
    """
    Function that gets the json response to our url request
    """
    get_books_url = 'https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=zXWZUr8x8WPVNP1ZKKsxeUOJRsMz7OUH'

    get_books_response = requests.get(get_books_url).json()
    if get_books_response['results']['books']:
        book_results_list = get_books_response['results']['books']
       
        books_list = []
        for book in book_results_list:
            rank = book.get("rank")
            title = book.get('title')
            author = book.get('author')
            poster = book.get('book_image')
            description = book.get('description')
            publisher = book.get('publisher')

            the_book = Books(rank, title, author, poster, description, publisher)
            books_list.append(the_book)
    return books_list
