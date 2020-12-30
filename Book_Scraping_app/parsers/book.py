import re
import logging
from locators.book_locators import BookLocators

logger = logging.getLogger('app.book')

class BookParser:

    RATINGS={ 'One': 1,
              'Two': 2,
              'Three': 3,
              'Four': 4,
              'Five': 5
        }


    def __init__(self,parent):
        logger.debug("Passing BeautifulSoup object")
        self.parent=parent    #BeautifulSoup object (html tag)

    @property
    def title(self):
        logger.debug("Finding book title")
        items=self.parent.select_one(BookLocators.title)
        item = items.attrs.get('title')
        logger.debug("Found book title")
        return item

    @property
    def link(self):
        logger.debug("Finding book link")
        items=self.parent.select_one(BookLocators.title)
        item = items.attrs.get('href')
        logger.debug("Found book link")
        return item

    @property
    def star(self):
        logger.debug("Finding book rating")
        items = self.parent.select_one(BookLocators.stars)
        item = items.attrs.get('class')
        rating = [x for x in item if x != 'star-rating']
        rating_star=BookParser.RATINGS[''.join(rating)]
        logger.debug("Found book rating")
        return rating_star

    @property
    def price(self):
        logger.debug("Finding book price")
        items = self.parent.select_one(BookLocators.price).string
        pattern='([0-9]+\.[0-9]+)'                            #one or more from the start,inlude the dot,one or more until the end
        matches=re.search(pattern,items)
        logger.debug("Found book price")
        return float(matches.group(1))

    def __repr__(self):
        return f'<Book {self.title}, costs ${self.price}, rates: {self.star} stars>'

