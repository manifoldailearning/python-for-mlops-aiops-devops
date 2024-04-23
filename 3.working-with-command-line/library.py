#!/usr/bin/env python
"""
Command-line tool for library management using argparse
"""
import argparse

def add_book(title, author):
    print(f"Adding book: '{title}' by {author}")

def find_books(query):
    # Simulate a database search
    books = [
        {'title': 'Pride and Prejudice', 'author': 'Jane Austen'},
        {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
        {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    ] 
    results = [book for book in books if query.lower() in book['title'].lower()]

    if results:
        print("Found the following books:")
        for book in results:
            print(f"  - {book['title']} by {book['author']}")
    else:
        print(f"No books found matching '{query}'")

def checkout(patron, title):
    print(f"Checking out '{title}' to {patron}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Library Management Tool')

    parser.add_argument('--verbose', '-v',   
                        help='Increase output',
                        action='store_true')

    subparsers = parser.add_subparsers(dest='func') 

    add_parser =  subparsers.add_parser('add',  
                                        help='Add a book to the catalog')
    add_parser.add_argument('title', help='Title of the book')
    add_parser.add_argument('author', help='Author of the book')

    search_parser = subparsers.add_parser('search', 
                                          help='Find books')
    search_parser.add_argument('query', help='Search query')

    checkout_parser = subparsers.add_parser('checkout',
                                            help='Check out a book')
    checkout_parser.add_argument('patron', help='Patron name')
    checkout_parser.add_argument('title', help='Title of the book')

    args = parser.parse_args()

    if args.func == 'add': 
        add_book(args.title, args.author)
    elif args.func == 'search':
        find_books(args.query)
    elif args.func == 'checkout':
        checkout(args.patron, args.title)
