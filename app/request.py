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
    # with urllib.request.urlopen(get_books_url) as url:
    #     get_books_data = url.read()
    #     get_books_response = json.loads(get_books_data)
    #     book_results = None
    get_books_response = requests.get(get_books_url).json()
    if get_books_response['results']['books']:
        book_results_list = get_books_response['results']['books']
        # book_results = process_results(book_results_list)
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
# def process_results(book_list):
#     """
#     Function  that processes the book result and transform them to a list of Objects
#     Args:
#         book_list: A list of dictionaries that contain book details
#     Returns :
#         book_results: A list of book objects
#     """
#     book_results = []
#     for book_item in book_list:
#         id = book_item.get('rank')
#         title = book_item.get('title')
#         author = book_item.get('author')
#         poster = book_item.get('book_image')
#         description = book_item.get('description')
#         publisher = book_item.get('publisher')


       
#         if poster:
#             book_object = Books(id,title, author, poster, description, publisher)
#             book_results.append(book_object)
#     return book_results

# def get_books():
#     get_book_details_url = base_url.format(id, api_key)
#     with urllib.request.urlopen(get_book_details_url) as url:
#         book_details_data = url.read()
#         book_details_response = json.loads(book_details_data)
#         book_object = None
#         if book_details_response:
#         id = book_item.get('id')
#         image_url = book_item.get('image_url')
#         title = book_item.get('original_title')
#         author = book_item.get('author')
#         text_reviews_count = book_item .get('text_reviews_count')
#         overview = book_item.get('overview')
#         poster = book_item.get('poster_path')
#         book_count = book_item .get('book_count')
#         rating_count = book_item .get('rating_count')
#         book_object = Book(id, image_url, title, author, text_reviews_count, overview, poster, book_count, rating_count)
#     return book_object

    