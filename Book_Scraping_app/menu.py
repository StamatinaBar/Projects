import logging
from app import books

logger = logging.getLogger('app.menu')

print("A BOOK SCRAPER APP")
options='''Choose from the following:
        press 1 for top books
        press 2 for cheapest books
        press 3 for the next book
        press q to exit
'''

def top_books():
    logger.info('Finding top books')
    top_books=sorted(books, key=lambda x: x.star, reverse=True)[:10]
    for top in top_books:
        print(top)

def cheapest_books():
    logger.info('Finding cheapest books')
    cheap_books = sorted(books, key=lambda x: x.price)[:10]
    for cheap in cheap_books:
        print(cheap)

book_generator=(book for book in books)

def next_book():
    logger.info('Finding next book')
    print(next(book_generator))

user_options = {'1': top_books,
              '2': cheapest_books,
              '3': next_book
              }


def menu():
    while True:
        user_input = input(options)
        if user_input in ('1','2','3'):
            user_options[user_input]()
        elif user_input=='q':
            break
        else:
            print("Not valid option.Try again")
            continue
    logger.debug('Program terminated')


menu()