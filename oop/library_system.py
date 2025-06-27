class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author

class EBook(Book):
    def __str__(self, title, author, file_size:int):
        super().__init__(title, author)
        if not isinstance(file_size,int) or file_size <=0:
            raise ValueError("File size must be a positive integer")
        
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self,title,author, pages:int):    
        super().__init__(title, author)
        if not isinstance(pages,int) or pages<=0:
            raise ValueError("Pages must be a positive integer")
        self.pages = pages    
class Library():
    def __init__(self):
        self.Book = []
        self.Ebook =[]
        self.PrintBook = []    

    def add_book(self, book):
        if isinstance(book, Ebook):
            self.Ebook.append(Book) 
        elif isinstance(book, PrintBook):
            self.PrintBook.append(book) 
        else:
            self.Book.append(book)

    def list_books(self):  
     print("Books in the Library:")
     for book in self.Book:
         print(f"Book: {book.title} by {book.author}")
     for ebook in self.Ebook:
             print(f"Ebook: {ebook.title} by {ebook.author}. File size: {ebook.file_size}MB")
     for print_book in self.PrintBook:
         print(f"Print Book: {print_book.title} by {print_book.author}. Pages: {print_book.pages}")         
                             
    