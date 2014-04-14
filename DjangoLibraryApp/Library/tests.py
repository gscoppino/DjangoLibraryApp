import datetime
from django.utils import timezone
from django.test import TestCase
from Library.models import User, Library, Shelf, Book

# Create your tests here.
class BookMethodTests(TestCase):
    def test_was_published_recently_with_old_book(self):
        time = timezone.now() - datetime.timedelta(days=31)
        past_book = Book(title='Past', author='Past', publisher='Past', pub_date=time)
        self.assertEqual(past_book.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_book(self):
        time = timezone.now() - datetime.timedelta(days=15)
        recent_book = Book(title='Recent', author='Recent', publisher='Recent', pub_date=time)
        self.assertEqual(recent_book.was_published_recently(), True)

    def test_was_published_recently_with_future_book(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_book = Book(title='Future', author='Future', publisher='Future', pub_date=time)
        self.assertEqual(future_book.was_published_recently(), False) 
