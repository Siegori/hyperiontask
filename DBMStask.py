import sqlite3
#Basic command t hat adds a book into the data base, or returns an error if you fail to enter the correct values or if there is
#an overlap in IDs
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

#This allows you to update a book by refrencing it's ID and then updating a specified value
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

#Much like update book, this simply deletes a single thing from the database
def delete_book():
    IDlookup = input("Please enter the ID of the book you wish to update")
    cursor.execute('''DELETE FROM books WHERE id = ?''', (IDlookup,))
    db.commit()

#This allows you find and display information of a specific book
def find_book():
    IDlookup = input("Please enter the ID of the book you wish to find")
    cursor.execute('''SELECT * FROM books WHERE id = ?''', (IDlookup,))
    book = cursor.fetchone()
    print(book)



#This displays every entry of the database for debug purposes.
def display_all():
    cursor.execute('''SELECT * FROM books''')
    books = cursor.fetchall()
    for book in books:
        print(book)
        
#This line of code opens up the database so you can begin working with it.
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

    if mode == 5:
        display_all()

    if mode == 0:
        exit()