import logging
import requests
from pages.books_page import BookPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt')

logger = logging.getLogger('app')

page = requests.get('https://books.toscrape.com')
book=BookPage(page)

books=book.books

for i in range(2,book.number_page):
    page_url =f"https://books.toscrape.com/catalogue/page-{i}.html"
    page = requests.get(page_url)
    logger.debug("Downloading page content.BookPage instance created")
    book = BookPage(page)
    books.extend(book.books)





