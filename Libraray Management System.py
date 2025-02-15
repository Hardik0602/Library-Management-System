# pip install mysql-connector-python
# pip uninstall mysql-connector-python
from datetime import date
import mysql.connector
db = mysql.connector.connect(
    host="localhost", # mysql host name
    user="Hardik", # mysql username
    password="MadCat", # mysql password
    database="hardik" # database with required tables
)
cursor = db.cursor()
def show_books():
    cursor.execute("SELECT book_id, title, author, quantity FROM books")
    books = cursor.fetchall()
    if not books:
        print("No books available.")
    else:
        print("Books Available:")
        for book in books:
            book_id, title, author, quantity = book
            print(f"ID: {book_id}, Title: {title}, Author: {author}, Quantity: {quantity}")
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    book_id = input("Enter the ID of the book: ")
    quantity = int(input("Enter the quantity of the book: "))
    cursor.execute("INSERT INTO books (title, author, book_id, quantity) VALUES (%s, %s, %s, %s)",
                   (title, author, book_id, quantity))
    db.commit()
    print("Book added successfully")
def issue_book():
    name = input("Enter your name: ")
    book_id = input("Enter the ID of the book to issue: ")
    issue_date = date.today()
    cursor.execute("INSERT INTO issue (name, book_id, issue_date) VALUES (%s, %s, %s)",
                   (name, book_id, issue_date))
    db.commit()
    print("Book issued to " + name)
    book_update_quantity(book_id, -1)
def submit_book():
    name = input("Enter your name: ")
    book_id = input("Enter the ID of the book to submit: ")
    submit_date = date.today()
    cursor.execute("INSERT INTO submit (name, book_id, submit_date) VALUES (%s, %s, %s)",
                   (name, book_id, submit_date))
    db.commit()
    print("Book submitted by " + name)
    book_update_quantity(book_id, 1)
def book_update_quantity(book_id, n):
    if n == 1:
        cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE book_id = %s", (book_id,))
    else:
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE book_id = %s", (book_id,))
    db.commit()
def remove_book():
    book_id = input("Enter the ID of the book to remove: ")
    cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
    db.commit()
    print("Book removed successfully")
def main():
    print("\n***** Library Management System *****")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Remove Book")
    print("4. Issue Book")
    print("5. Submit Book")
    print("6. Exit")
while True:
    main()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_book()
    elif choice == '2':
        show_books()
    elif choice == '3':
        remove_book()
    elif choice == '4':
        issue_book()
    elif choice == '5':
        submit_book()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")