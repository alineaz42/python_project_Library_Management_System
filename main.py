# ___________________Library Management System___________________
# ****************************Ali Neaz****************************

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
                f"You have been issued {bookName}. Please keep it safe and return within 15 days ")
            self.books.remove(bookName)
            return True
        else:
            print(
                "Sorry, This book is either not availabe or  already issued to someone else. Wait until the book is returned")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")


class Student:

    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow:")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return :")
        return self.book


if __name__ == "__main__":
    centralLibray = Library(
        ["Algorithms", "Django", "Clrs", "Python Notes", "Java", "C++"])
    student = Student()

    while True:
        welcomeMsg = '''******Welcome to Central Library******
        Please choose an option:
        1. List all the availabe books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choise: "))
        if a == 1:
            centralLibray.displayAvailabeBooks()
        elif a == 2:
            centralLibray.borroBook(student.requestBook())
        elif a == 3:
            centralLibray.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library.")
            exit()
        else:
            print("Invalid Choice")
