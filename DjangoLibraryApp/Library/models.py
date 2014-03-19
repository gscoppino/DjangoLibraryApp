from django.db import models

# Used to handle model edge-cases
from django.core.exceptions import ValidationError

# For use in time related calculations
from django.utils import timezone
import datetime

class Library(models.Model):

    def __unicode__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    max_shelves = models.IntegerField(default=0)
    max_books = models.IntegerField(default=0)
    
    def shelves(self):
        return self.shelf_set.count()

    def books(self):
        num_books = 0
        for shelf in self.shelf_set.all():
            num_books += shelf.book_set.count()
        return num_books

class Shelf(models.Model):
    
    def __unicode__(self):
        return self.library.name + "_" + self.shelf_code

    library = models.ForeignKey(Library)
    shelf_code = models.CharField(max_length=5)
    max_books = models.IntegerField(default=0)

    def books(self):
        return self.book_set.count()
  
    def clean(self):
        if self.library.shelves() == self.library.max_shelves:
            raise ValidationError("Failed to add shelf to library; library is at shelf capacity!")
        if self.library.books() + self.books() > self.library.max_books:
            raise ValidationError("Failed to add shelf to library; library is at book capacity!")
    
class Book(models.Model):
    
    def __unicode__(self):
        return self.title
    
    shelf = models.ForeignKey(Shelf, null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=25, blank=True)
    publisher = models.CharField(max_length=100)
    pub_date = models.DateField('Date published')
    isbn = models.CharField(max_length=20)
    condition = models.CharField(max_length=10, blank=True)
    checkout_status = models.BooleanField(default=False)

    def availability(self):
        if self.checkout_status == True:
            return "Checked Out"
        else:
            return "Available"
    availability.admin_order_field = "checkout_status"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=30)
    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.short_description = "Published Recently?"
    was_published_recently.boolean = True

    def clean(self): 
        if self.shelf and self.shelf.books() == self.shelf.max_books:
            raise ValidationError("Failed to add book to shelf; shelf is full!")
