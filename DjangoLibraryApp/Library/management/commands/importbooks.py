#####################################################
# Authors: Giuseppe Scoppino, Johnathon Monson 2014 #
#####################################################

import os
import sys, traceback
import django

from django.core.management.base import BaseCommand, CommandError
from Library.models import Book

class Command(BaseCommand):
    args = '<filename ...>'
    help = 'Import books into the database from a specified CSV file.'

    def handle(self, *args, **options):
        for argfile in args:
            try: 
                if os.path.exists(argfile):
                    with open(argfile, 'r') as f: 
                        for line in f:
                            data = line.split (",", 6)

                            book_title= data[0].strip()[0:97]
                            if len(book_title) == 97:
                                book_title += '...'
                            book_author = data[1].strip()[0:97]
                            if len(book_author) == 97:
                                book_author += '...'
                            book_pub_date = data[2].strip() + "-01-01"
                            book_publisher = data[4].strip()[0:97]
                            if len(book_publisher) == 97:
                                book_publisher += '...'
                            book_isbn = data[5].strip()
                            book = Book(title=book_title, 
                                        author=book_author, 
                                        pub_date=book_pub_date, 
                                        publisher=book_publisher, 
                                        isbn=book_isbn)
                            book.save()
                    print "All books from " + argfile + " imported."
                else:
                    print "No such file " + argfile + "."
            except:
                raise CommandError('Fail! Reason\n %s\n %s' % 
                                   str(sys.exc_info()),
                                   str(traceback.format_exc()))
    
