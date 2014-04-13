import django
from Library.models import Library, Shelf, Book

north_side = Library(name='North Side', max_shelves=50, max_books=1000)
south_side = Library(name='South Side', max_shelves=100, max_books=5000)
west_side = Library(name='West Side', max_shelves=50, max_books=1000)
east_side = Library(name='East Side', max_shelves=25, max_books=500)

north_side.save()
south_side.save()
west_side.save()
east_side.save()

north_side_1a = Shelf(library=north_side, shelf_code='1A', max_books=50)
north_side_1b = Shelf(library=north_side, shelf_code='1B', max_books=50)
south_side_1a = Shelf(library=south_side, shelf_code='1A', max_books=50)
south_side_1b = Shelf(library=south_side, shelf_code='1B', max_books=50)
west_side_1a = Shelf(library=west_side, shelf_code='1A', max_books=50)
west_side_1b = Shelf(library=west_side, shelf_code='1B', max_books=50)
east_side_1a = Shelf(library=east_side, shelf_code='1A', max_books=50)
east_side_1b = Shelf(library=east_side, shelf_code='1B', max_books=50)

north_side_1a.save()
north_side_1b.save()
south_side_1a.save()
south_side_1b.save()
west_side_1a.save()
west_side_1b.save()
east_side_1a.save()
east_side_1b.save()

books = Book.objects.order_by('?')[:5]
for book in books:
    book.shelf=north_side_1a
    book.save()

books = Book.objects.order_by('?')[:5]
for book in books:
    book.shelf=north_side_1b
    book.save()

books = Book.objects.order_by('?')[:5]
for book in books:
    book.shelf=south_side_1b
    book.save()

books = Book.objects.order_by('?')[:5]
for book in books:
    book.shelf=south_side_1a
    book.save()

books = Book.objects.order_by('?')[:5]
for book in books:
    book.shelf=east_side_1a
    book.save()

books = Book.objects.order_by('?')[:5]
for book in books:
    book.shelf=east_side_1b
    book.save()

books = Book.objects.order_by('?')[:5]
for book in books:
    book.shelf=west_side_1b
    book.save()

books = Book.objects.order_by('?')[:5]
for book in books:
    book.shelf=west_side_1b
    book.save()
