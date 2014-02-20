from django.db import models

# For use in time related calculations
from django.utils import timezone
import datetime

class Library(models.Model):

    def __unicode__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    shelf_capacity = models.IntegerField(default=0)
    book_capacity = models.IntegerField(default=0)

class Shelf(models.Model):
    
    def __unicode__(self):
        return self.shelf_code

    library = models.ForeignKey(Library)
    shelf_code = models.CharField(max_length=5)
    book_capacity = models.IntegerField(default=0)
    
class Book(models.Model):
    
    def __unicode__(self):
        return self.title
    
    libraries = models.ManyToManyField(Library)
    shelves = models.ManyToManyField(Shelf)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=25)
    publisher = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Date published')
    isbn = models.CharField(max_length=20)
    copies = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now - datetime.timedelta(days=30)