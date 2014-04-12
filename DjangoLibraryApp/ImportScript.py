import os.path
import django
from Library.models import Book

if os.path.exists("BookList.txt"):
    file = open("BookList.txt","r+")
    #Take each line with readline until EOF and assign to string and sort.
    for line in file:
        book = line.split (",", 6)
        print book

        book_title= book[0].strip()
        book_author = book[1].strip()
        book_pub_date = book[2].strip() + "-01-01"
        book_publisher = book[4].strip()
        book_isbn = book[5].strip()
        
        book_object = Book(title=book_title, author=book_author, pub_date=book_pub_date, publisher=book_publisher,
                    isbn=book_isbn)
        book_object.save()
    #Remove the file to allow a new file to be placed into here without any problems
    os.remove("BookList.txt")
else:
    print "There is nothing to import"
