import fire

class Library:
    def __init__(self):
        self.books = {
            "Adventure": ["Treasure Island", "Moby Dick"],
            "Fantasy": ["The Hobbit", "The Lord of the Rings"],
        }

    def add_book(self, title, category):
        if category in self.books:
            self.books[category].append(title)
        else:
            self.books[category] = [title]
        print(f"{title} added to the '{category}' section")

    def list_books(self, category=None):
        if category:
            if category in self.books:
                print(f"Books in the '{category}' section:")
                for book in self.books[category]:
                    print(book)
            else:
                print(f"Category '{category}' not found")
        else:
            print("All Books:")
            for category, books in self.books.items():
                print(f"  {category}: {', '.join(books)}")

def checkout(book_title, patron):
    # Simulating book checkout (add more logic later if needed)
    print(f"{patron} has checked out '{book_title}'")


class LibraryCLI:
    def __init__(self):
        self.library = Library()
        self.checkout = checkout 

if __name__ == '__main__':
    fire.Fire(LibraryCLI) 
