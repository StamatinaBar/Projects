from utils import database_sql


user_menu=['0','1','2','3','q']

class NotInTheListBook(Exception):
    def __init__(self,book):
        super().__init__(f"The book--> '{book}' is not in list!")


def menu():
    database_sql.database_exists()
    while True:
        print("========Welcome to Bookstore app!==========")
        print("Do you want to retrieve, enter, mark or delete a book?")
        user_input=input("Choose 0,1,2,3 respectively or q to quit ")
        if user_input=='0':
            database_sql.retrieve_book()
        elif user_input=='1':
            name,author=input("Press name#author ").split('#')
            database_sql.enter_book(name,author)
        elif user_input=='2':
            name=input("Type the book you read ")
            database_sql.mark_as_read(name)
        elif user_input=='3':
            name=input("Type the name of the book you want to delete ")
            database_sql.delete_book(name)
        elif user_input not in user_menu:
            print("Not valid input!Try again")
            continue
        elif user_input=='q':
            print("Thank you!")
            break


menu()