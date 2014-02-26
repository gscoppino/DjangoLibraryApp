from Library.models import Library, Shelf, Book
from sys import argv
from os.path import exists

script, filename = argv

if exists(filename)
    file = open(filename)

for line in file:
    //evaluate struct of line using regex
    //if valid, add model to db
    //if not, terminate at said line