from models import Book
from storage import FileStorage

class BookManager:
    def __init__(self, storage: FileStorage):
        self.storage = storage
        self.books = self.storage.load()

    def add_book(self, book: Book):
        self.books[book.book_id] = book.__dict__
        self.storage.save(self.books)

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            self.storage.save(self.books)
            print("✅ Book removed successfully.")
        else:
            print("⚠️ Book doesn't exist.")

    def borrow_book(self, book_id):
        if book_id in self.books and not self.books[book_id]["is_borrowed"]:
            self.books[book_id]["is_borrowed"] = True
            self.storage.save(self.books)
            print(f"📕 {self.books[book_id]['title']} borrowed successfully.")
        else:
            print("⚠️ Book not available or already borrowed.")

    def return_book(self, book_id):
        if book_id in self.books and self.books[book_id]["is_borrowed"]:
            self.books[book_id]["is_borrowed"] = False
            self.storage.save(self.books)
            print(f"📗 {self.books[book_id]['title']} returned successfully.")
        else:
            print("⚠️ Book was not borrowed or doesn't exist.")

    def list_books(self):
        if not self.books:
            print("📂 No books in the library.")
            return
        for book_id, book in self.books.items():
            status = "Borrowed" if book["is_borrowed"] else "Available"
            print(f"{book_id}: {book['title']} by {book['author']} ({book['year']}) - {status}")
