"""
class : Book
attributes : book, title, author, isbn, availability
methods : checkAvailability, returnBook, borrow
"""

class Book():
    def __init__(self, title, author, isbn, availability):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability

    def borrow(self):
        print(f"\nUser has now borrowed {self.title} by {self.author}")

    def returnBook(self):
        print("Book has been returned.")

    def checkAvailability(self):
        if self.availability == False:
            print(f"\n {self.title} is currently available.")
        else:
            print(f"\n{self.title} by {self.author} is available")

            choice = input(f"\nWould the user like to borrow this book? (y or n):")

            if choice.lower() == "y":
                self.borrow()
            elif choice.lower() == "n":
                print("End.")
            else:
                print("Invalid input.")

firstBook = Book("Game of Thrones", "G.R.R. Martin", 987612, True)

firstBook.checkAvailability()
firstBook.returnBook()