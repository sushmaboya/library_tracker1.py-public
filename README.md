📚 Book Tracker
A Python-based Book Management System that allows users to add, remove, borrow, return, and list books with data stored persistently in a JSON file.
This project demonstrates Object-Oriented Programming (OOP) concepts, file handling, and simple data management through a command-line interface (CLI).
🧠 Features
➕ Add Books: Save new book details (ID, title, author, year).
❌ Remove Books: Delete unwanted book entries.
📖 Borrow & Return: Update the borrowed status of books dynamically.
📋 List Books: Display all stored books with their details.
💾 Persistent Storage: All data is saved in a local JSON file (books.json).
🧩 Project Structure:
📁 BookTracker/
│
├── __init__.py      # Makes the folder a Python package
├── main.py          # Main CLI program (entry point)
├── manager.py       # Handles all book management logic
├── models.py        # Defines the Book class
├── storage.py       # Handles JSON file saving/loading
└── books.json       # Data file storing book records
⚙️ How It Works
1.Run the program:
python main.py
2.Choose from the menu options:
1. Add Book
2. Remove Book
3. Borrow Book
4. Return Book
5. List Books
6. Exit
3.All updates are automatically stored in books.json.
🧰 Technologies Used
Language: Python 3
Modules: json (for storage handling)
Paradigm: Object-Oriented Programming (OOP)
📘 Sample Data (books.json)
{
    "101": {
        "book_id": "101",
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "year": "1997",
        "is_borrowed": false
    },
    "102": {
        "book_id": "102",
        "title": "Telugu",
        "author": "Sushma",
        "year": "2000",
        "is_borrowed": false
    }
}
🏗️ Concepts Demonstrated
Classes and Objects
File Handling (JSON)
CRUD Operations
Modular Programming
Data Persistence
🚀 Future Enhancements
Add a search feature (by title or author)
Build a Graphical User Interface (GUI) using Tkinter or Streamlit
Add user authentication and borrowing history tracking
👩‍💻 Author
Sushma Boya
📧 sushmaboya11@gmail.com
💼 https://github.com/sushmaboya
