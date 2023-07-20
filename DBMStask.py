import sqlite3

#Simple function that asks for 4 inputs then uses those 4 inputs to add a book into the database.
#NOTE: find a way to make the ID's unique
def add_book():
    bookid = int(input("What is the book ID?"))
    bookname = input("What is the book title?")
    bookauthor = input("What is the book author")
    bookquant = int(input("What is the book quantity?"))
    try:
        cursor.execute('''IF NOT EXISTS INSERT INTO books(id, Title, Author, Qty)''', (bookid, bookname, bookauthor, bookquant))
    except sqlite3.OperationalError:
        print("An error occured, please enter the correct values")
    finally:
        db.commit()

#This prompts fo an input, then asks what value you want to change for the book with the matching ID
#Then it executes the command using the previous inputs to change the desired object
def update_book():
    IDlookup = input("Please enter the ID of the book you wish to update")
    mode = int(input("What do you want to update?"))
    if mode == 1:
        newvalue = int(input("What is the new value you want?"))
        cursor.execute('''UPDATE books SET id = ? FROM book where id = ? VALUES(?,?)''', (newvalue, IDlookup))
        db.commit()
    elif mode == 2:
        newvalue = input("What is the new value you want?")
        cursor.execute('''UPDATE books SET Title = ? FROM book where id = ? VALUES(?,?)''', (newvalue, IDlookup))
        db.commit()
    elif mode == 3:
        newvalue = input("What is the new value you want?")
        cursor.execute('''UPDATE books SET Author = ? FROM book where id = ? VALUES(?,?)''', (newvalue, IDlookup))
        db.commit()
    else:
        newvalue = int(input("What is the new value you want?"))
        cursor.execute('''UPDATE books SET Qty = ? FROM book where id = ? VALUES(?,?)''', (newvalue, IDlookup))
        db.commit()


#simple delete command
def delete_book():
    IDlookup = input("Please enter the ID of the book you wish to update")
    cursor.execute('''DELETE FROM books where id = ? VALUES(?)''', IDlookup)
    db.commit()

#Finds and prints a book
def find_book():
    IDlookup = input("Please enter the ID of the book you wish to update")
    cursor.execute('''SELECT * FROM books where id = ? VALUES(?)''', IDlookup)
    book = cursor.fetchone()
    print(book)


#Creating and connecting to a database
db = sqlite3.connect('data/ebookstore')

cursor = db.cursor()

cursor.execute('''CREATE DATABASE IF NOT EXISTS ebookstore''')
db.commit()

cursor.execute('''CREATE TABLE books (id bigint PRIMARY KEY, Title varchar(500), Author varchar(60), Qty (int)''')
db.commit()

#Creating the book using a tuble and then using the executemany to create the test table
books = [(3001, "A Tale of Two Cities", "Charles Dickens", 30),
         (3002, "Harry Potter and the Philosopher's stone", "J.K Rowling", 40),
         (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
         (3004, "Lord of the Rings", "J.R.R. Tolkien", 37),
         (3005, "Alice in Wonderland", "Lewis Carroll", 12)
         ]
cursor.executemany('''INSERT INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''', books)
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
