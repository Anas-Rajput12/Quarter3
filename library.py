import os
import json

# Load the library from file if it exists
def load_library(filename="library.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Save the library to file
def save_library(library, filename="library.txt"):
    with open(filename, "w") as file:
        json.dump(library, file, indent=4)

# Display the menu
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Add a book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    try:
        year = int(input("Enter the publication year: ").strip())
    except ValueError:
        print("Invalid year. Please enter a number.")
        return
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = read_input == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        search = input("Enter the title: ").strip().lower()
        results = [book for book in library if search in book["title"].lower()]
    elif choice == "2":
        search = input("Enter the author: ").strip().lower()
        results = [book for book in library if search in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if results:
        print("\nMatching Books:")
        for i, book in enumerate(results, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

# Display all books
def display_all_books(library):
    if not library:
        print("Your library is empty.")
        return
    print("\nYour Library:")
    for i, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Display statistics
def display_statistics(library):
    total = len(library)
    if total == 0:
        print("No books in library to show statistics.")
        return
    read_books = sum(1 for book in library if book["read"])
    percent = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percent:.1f}%")

# Main loop
def main():
    library = load_library()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
