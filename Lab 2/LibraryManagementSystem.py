class Book:
    def __init__(self, title, author, isbn):
        self.title= title
        self.author= author
        self.isbn= isbn
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getIsbn(self):
        return self.isbn
    

    def setTitle(self, x):
        self.title= x
    def setAuthor(self, y):
        self.author= y
    def setIsbn(self, x):
        self.isbn= x
    def __str__(self):
        return f"Title: {self.title}\nAuthor:{self.author}\nISBN:{self.isbn}"
    

class Library:
    def __init__(self):
        self.bookList= dict()

    def add_book(self, book):
        self.bookList[book.isbn]= book 

    def remove_book(self, x):
        self.bookList[x].pop()
    
    def searchByTitle( self, title):
        for key in self.bookList:
            tempTitle= self.bookList[key].title
            if(title == tempTitle):
                return self.bookList[key]
    def displayBooks ( self):
        for key in self.bookList:
            tempBook= self.bookList[key]
            print(tempBook)
            print("\n")

book1= Book("Belafurabar age", "Arif Azad", "123")
book2= Book("a", "Tamim", "124")
book3= Book("v", "Nahid", "143")

myLibrary= Library()
myLibrary.add_book(book1)
myLibrary.add_book(book2)
myLibrary.add_book(book3)

myLibrary.displayBooks()

temp= myLibrary.searchByTitle("Belafurabar age")
print(temp)

