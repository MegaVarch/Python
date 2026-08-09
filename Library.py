books = ["Harry Potter", "Diary of a Wimpy Kid", "The Hobbit", "Percy Jackson"]
copies = [3, 0, 2, 5]

library = list(zip(books, copies))

print("Library:")
for book, copy in library:
    print(book, "-", copy, "copies")

# Filter available books
available = list(filter(lambda x: x[1] > 0, library))

print("\nAvailable books:")
for book, copy in available:
    print(book)

# Update late fees using map()
fees = [10, 20, 30, 40]

updated_fees = list(map(lambda fee: fee + 5, fees))

print("\nUpdated late fees:", updated_fees)

# Check a chosen book
chosen = input("\nEnter a book name: ")

for book, copy in library:
    if book == chosen:
        if copy == 0:
            print("Book is unavailable!")
            break
        else:
            print("Book is available!")
            break
else:
    print("Book not found.")