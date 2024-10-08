# Library Management System

# Step 1: Setting up data structures
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "status": "Available"},
    {"id": 2, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "status": "Checked Out"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "status": "Available"}
]

users = [
    {"id": 1, "name": "Alice", "borrowed_books": []},
    {"id": 2, "name": "Bob", "borrowed_books": [2]}
]

# Step 2: Viewing books
def view_books():
    print("\nAll Books:")
    for book in books:
        print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({book["status"]})')

# Step 3: Searching for books
def search_books():
    search_by = input("Search by (title/author/genre): ").strip().lower()
    query = input(f"Enter the {search_by}: ").strip().lower()
    
    print(f"\nBooks matching {search_by}:")
    for book in books:
        if query in book[search_by].lower():
            print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({book["status"]})')

# Step 4: Borrowing books
def borrow_book():
    user_id = int(input("Enter your User ID: "))
    book_id = int(input("Enter the Book ID you want to borrow: "))
    
    user = next((user for user in users if user["id"] == user_id), None)
    book = next((book for book in books if book["id"] == book_id), None)
    
    if user and book:
        if book["status"] == "Available":
            book["status"] = "Checked Out"
            user["borrowed_books"].append(book_id)
            print(f'You have borrowed "{book["title"]}".')
        else:
            print(f'Sorry, the book "{book["title"]}" is currently checked out.')
    else:
        print("Invalid User ID or Book ID.")

# Step 5: Returning books
def return_book():
    user_id = int(input("Enter your User ID: "))
    book_id = int(input("Enter the Book ID you want to return: "))
    
    user = next((user for user in users if user["id"] == user_id), None)
    book = next((book for book in books if book["id"] == book_id), None)
    
    if user and book and book_id in user["borrowed_books"]:
        book["status"] = "Available"
        user["borrowed_books"].remove(book_id)
        print(f'You have returned "{book["title"]}".')
    else:
        print("Invalid User ID or Book ID, or you didn't borrow this book.")

# Step 6: Viewing users
def view_users():
    print("\nAll Users:")
    for user in users:
        borrowed_books = ", ".join(str(book_id) for book_id in user["borrowed_books"]) or "None"
        print(f'User ID: {user["id"]}, Name: {user["name"]}, Borrowed Books: {borrowed_books}')

# Step 7: Main Menu
def main_menu():
    while True:
        print("\nWelcome to the Community Library System!")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all users")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            view_books()
        elif choice == "2":
            search_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_users()
        elif choice == "6":
            print("Exiting the Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Running the Library Management System
main_menu()
