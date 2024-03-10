#initalize empty lists, set and dictionary
books_list = []
authors_set = set()
books_dict = {}

#add books
books_list.append("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"] = "John Smith"

books_list.append("Data and structure Algorythms")
authors_set.add("Jane Doe")
books_dict["Data Structure and Algorythms"] = "John Smith"

books_list.append("Machine Learning Basics")
authors_set.add("Alice Jhonsoon")
books_dict["Machine Learning Basics"] = "Alice Johnson"

#search for a book
search_title = input("Enter the Title of the Book to Search")
if search_title in books_list:
    print(f"Book Found! Author: {books_dict[search_title]}")
else:
    print("Book not Found!")

    #Display all books
    print("List of Books:")
    for book in books_list:
        print(book)

        #Remove a book
        remove_title = input("Enter the Title of the Book to Remove or Else Skip")
        if remove_title in books_list:
            remove_author = books_dict[remove_title]
            books_list.remove(remove_title)
            authors_set.remove(remove_author)
            del books_dict[remove_title]
            print("Books Removed Successfuly!")
            print("Books Available:", books_list)

        else:
            print("Books not found")

            