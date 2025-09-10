lib = {}
def add(book_id, title):
    if book_id in lib:
        print("Book ID already exists.")
    else:
        lib[book_id] = title
        print("Book added.")
def remove(book_id):
    if book_id in lib:
        del lib[book_id]
        print("Book removed.")
    else:
        print("Book ID not found.")
def search(book_id):
    if book_id in lib:
        print(f"Book found: {lib[book_id]}")
    else:
        print("Book not found.")
def update(book_id, new_title):
    if book_id in lib:
        lib[book_id] = new_title
        print("Book title updated.")
    else:
        print("Book ID not found.")
def display():
    if lib:
        print("Library Books:")
        for book_id, title in lib.items():
            print(f"{book_id}: {title}")
    else:
        print("Library is empty.")
def count():
    print("Total number of books:", len(lib))
def check(title):
    if title in lib.values():
        print("Title exists in the library.")
    else:
        print("Title not found.")
while True:
    print("\nLibrary Management System")
    print("1. Add")
    print("2. Remove")
    print("3. Search")
    print("4. Update")
    print("5. Display")
    print("6. Count")
    print("7. Check")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        add(book_id, title)
    elif choice == '2':
        book_id = input("Enter Book ID to remove: ")
        remove(book_id)
    elif choice == '3':
        book_id = input("Enter Book ID to search: ")
        search(book_id)
    elif choice == '4':
        book_id = input("Enter Book ID to update: ")
        new_title = input("Enter new title: ")
        update(book_id, new_title)
    elif choice == '5':
        display()
    elif choice == '6':
        count()
    elif choice == '7':
        title = input("Enter title to search: ")
        check(title)
    elif choice == '8':
        break
    else:
        print("Invalid choice")
        break
