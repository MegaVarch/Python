class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'Successfully returned:"{self.title}"')
        else:
            print(f'"{self.title}was not checked out')

book1 = Book("Wings of Fire", "Tui.T.Sutherland")
book2 = Book("Dune", "Frank Herbert")
book3 = Book("Wild Robot", "John Swcheinsteiger")

print("Library Activity")
book1.borrow_book()
book2.borrow_book()
book3.borrow_book()