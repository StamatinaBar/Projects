#from .database_manager(relative import)

from utils.database_manager import DatabaseManager

def database_exists() -> None:
    with DatabaseManager() as conn: # instead of calling connect,commit,close
        cursor = conn.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS BOOKS(
                 Name TEXT PRIMARY KEY,
                 Author TEXT,
                Read INT 
              )'''
        cursor.execute(sql)

def retrieve_book() -> None:
    with DatabaseManager() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM BOOKS")
        books = cursor.fetchall()
        count = 1
        for book in books:
            print(f"=========BOOK {count}===========")
            count += 1
            print(f"name: {book[0]} author: {book[1]} read: {book[2]}")
        print('                      ')


def enter_book(name: str,author: str) -> None:
    with DatabaseManager() as conn:
        cursor = conn.cursor()
        sql = "INSERT INTO BOOKS VALUES(?,?,0)"
        cursor.execute(sql,(name,author))


def mark_as_read(name: str) -> None:
    with DatabaseManager() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM BOOKS WHERE Name=?",(name,))
        books = cursor.fetchall()
        for book in books:
            if book[0]==name and book[2]==0:
                cursor.execute("UPDATE BOOKS SET Read=1 WHERE Name=?",(name,))
                print(f"You read '{book[0]}' (read=1)")
            elif book[0]==name and book[2]==1:
                print("You have already read this!")


def delete_book(name: str) -> None:
    with DatabaseManager() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM BOOKS WHERE Name=?", (name,))


