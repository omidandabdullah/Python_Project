
books = []
def list_of_book():
    book = input("Enter the name of your book: ")
    author = input("Enter the name of author: ")
    year = int(input("Enter the year of published:  "))
    isbn = int(input("Enter the number of isbn: "))
    price = float(input("Enter the price: "))
    save_book = (book,author,year,isbn,price)
    books.append(save_book)
    print("Saved succesfully")

#function of editing
def edit_books():
    isbn = input("Enter the number of isbn number if you want to update:  ")
    for save_book in books:
        if save_book[3] == isbn:
            books.remove(book)
            book = input("Enter the name of your book: ")
            author = input("Enter the name of author: ")
            year = int(input("Enter the year of published:  "))
            isbn = int(input("Enter the number of isbn: "))
            price = float(input("Enter the price: "))
            save_book = (book, author, year, isbn, price)
            books.append(save_book)
            print("Updated succesfully")
        else:
            print("book not found ")

#printing the all saved books
def print_book():
    print("Book Name\tAuthor Name\tPublisher\tISBN\tPrice")
    for save_book in books:
        print(save_book[0]+"\t"+save_book[1]+"\t"+str(save_book[2])+"\t"+str(save_book[3])+"\t"+str(save_book[4]))

while True:
    print("1. Add new book")
    print("2. Update books")
    print("3. print books")
    print("4. Exit")
    number = input("Choose the number:  ")
    if number == "1":
        list_of_book()
    elif number == "2":
        edit_books()
    elif number == "3":
        print_book()
    else:
        break
1








