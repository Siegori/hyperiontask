import sqlite3

def add_book():
    bookid = int(input("What is the book ID?"))
    bookname = input("What is the book title?")
    bookauthor = input("What is the book author")
    bookquant = int(input("What is the book quantity?"))
    try:
        cursor.execute('''INSERT OR IGNORE INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''', (bookid, bookname, bookauthor, bookquant))
    except sqlite3.OperationalError:
        print("An error occured, please enter the correct values")
    finally:
        db.commit()

def update_book():
    IDlookup = input("Please enter the ID of the book you wish to update")
    mode = int(input('''What do you want to update?
    1 - Update ID
    2 - Update Title
    3 - Update Author
    4 - Update Quantity'''))
    if mode == 1:
        newvalue = int(input("What is the new value you want?"))
        cursor.execute('''UPDATE books SET id = ? WHERE id = ?''', (newvalue, IDlookup))
        db.commit()
    elif mode == 2:
        newvalue = input("What is the new value you want?")
        cursor.execute('''UPDATE books SET Title = ? WHERE id = ?''', (newvalue, IDlookup))
        db.commit()
    elif mode == 3:
        newvalue = input("What is the new value you want?")
        cursor.execute('''UPDATE books SET Author = ? WHERE id = ?''', (newvalue, IDlookup))
        db.commit()
    elif mode == 4:
        newvalue = int(input("What is the new value you want?"))
        cursor.execute('''UPDATE books SET Qty = ? WHERE id = ?''', (newvalue, IDlookup))
        db.commit()
    else:
        print("Please enter a correct mode")

def delete_book():
    IDlookup = input("Please enter the ID of the book you wish to update")
    cursor.execute('''DELETE FROM books WHERE id = ?''', (IDlookup,))
    db.commit()

def find_book():
    IDlookup = input("Please enter the ID of the book you wish to update")
    cursor.execute('''SELECT * FROM books WHERE id = ?''', (IDlookup,))
    book = cursor.fetchone()
    print(book)

db = sqlite3.connect('data/ebookstore.db')

cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)''')
db.commit()

#Simple console for the DBMS
while True:
    print('''
    1. Enter Book
    2. Update Book
    3. Delete Book
    4. Search books
    0 Exit.
    : ''')

    mode = int(input("Please select an option"))

    if mode == 1:
        add_book()

    if mode == 2:
        update_book()

    if mode == 3:
        delete_book()

    if mode == 4:
        find_book()

    if mode == 0:
        exit()
