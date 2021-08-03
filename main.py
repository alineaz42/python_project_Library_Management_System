# ___________________Library Management System___________________


class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailabeBooks(self):
        print("Books availabe are: ")
        for book in self.books:
            print("\t *", book)

    def borroBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued{bookName}. Please keep it safe and return within 15 days ")
            self.books.remove(bookName)
        else:
            print(
                "Sorry, This book is already issued to someone else. Wait until the book is returned")


class Student:
    pass


if __name__ == "__main__":
    centralLibray = Library(
        ["Algorithms", "Django", "Clrs", "Python Notes", "Java", "C++"])
    centralLibray.displayAvailabeBooks()
