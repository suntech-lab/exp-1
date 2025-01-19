request = input("What is your request?")

if request == "borrow":
    book = input("What is the book title?")

    if len(book) > 10:
        print("Sorry. That book is not in our records.")
    else:
        print("Book reserved!")