#This is a Library system.
List_of_books = ["sherlock holmes","The lord of the rings", "IT","Six of crows","The hobbit","The last wish","The sword of destiny","A game of thrones","A song of fire and ice collection","The witcher collection"]
def book_display():
    
    print("The books that are available in our library are as follows:")
    for books in List_of_books:
          print(books)
    return List_of_books
          
def take_book():
    global List_of_books
    t_book = input("Enter the name of the book:")
    if t_book in List_of_books:
        List_of_books.remove(t_book)
        print("Thanks for taking the book!")
    else:
        print("The book that you want is not available!")
    return t_book
          
def return_book():
    global r_book
    r_book = input("Enter The name of the book that you wanth to return:")
    if r_book not in List_of_books:
        List_of_books.append(r_book)
        print("Thanks for returning the book!")
    else:
        print("The book that you mentioned is invalid!")
    return r_book
          
print("******Welcome to my library******")
print("------Main menu------")
print("Enter 1 for the display of available books")
print("Enter 2 to take a book")
print("Enter 3 to return a book")
print("Enter 4 to quit")
          
while True:
    b_code = int(input("Enter browsing code:"))
                 
    if b_code == 1:
        book_display()
        print("------------------------------------------")
        response = input("do you wish to continue? [y/n]")
        if response == "n":
            break
    elif b_code == 2:
        take_book()
        print("------------------------------------------")
        response = input("do you wish to continue? [y/n]")
        if response == "n":
            break
    elif b_code == 3:
        return_book()
        print("------------------------------------------")
        response = input("do you wish to continue? [y/n]")
        if response == "n":
            break
    elif b_code == 4:
        break
        
print("Thanks for shopping please visit again!")
    
