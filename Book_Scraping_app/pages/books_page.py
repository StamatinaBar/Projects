import logging
from bs4 import BeautifulSoup
from locators.books_page_locators import BooksPageLocators
from parsers.book import BookParser


logger = logging.getLogger('app.books_page')

class BookPage:
    def __init__(self,page):
        logger.debug("Creating HTML parser")
        self.soup = BeautifulSoup(page.content, "html.parser")

    @property
    def books(self):
        logger.debug("Searching all books in the page")
        items=self.soup.select(BooksPageLocators.books_page)    #BeautifulSoup object (html tag)
        items_list=[BookParser(item) for item in items]
        return items_list

    @property
    def number_page(self):
        logger.debug("Extracting total number of pages")
        items = self.soup.select(BooksPageLocators.page)
        items=[i.string for i in items if i.string!='1']
        items=sorted(items)
        logger.info(f"Lists of total books and books/page: `{items}`")
        x=int(items[0]) // int(items[1])
        logger.info(f"Found total book pages `{x}`")
        return x