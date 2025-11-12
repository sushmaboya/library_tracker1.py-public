from manager import BookManager
from storage import FileStorage
from models import Book

def main():
    storage = FileStorage("books.json")
    manager = BookManager(storage)

    while True:
        print("\n📚 Book Tracker Menu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            year = input("Enter Year: ")
            book = Book(book_id, title, author, year)
            manager.add_book(book)

        elif choice == "2":
            book_id = input("Enter Book ID to remove: ")
            manager.remove_book(book_id)

        elif choice == "3":
            book_id = input("Enter Book ID to borrow: ")
            manager.borrow_book(book_id)

        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            manager.return_book(book_id)

        elif choice == "5":
            manager.list_books()

        elif choice == "6":
            print("👋 Exiting Book Tracker. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
