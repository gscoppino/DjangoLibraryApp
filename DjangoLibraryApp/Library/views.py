from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from Library.models import * 
# Create your views here.
class IndexView(generic.ListView):
    model = Library 
    template_name = 'Library/index.html'
    context_object_name = 'home_data'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['library_list'] = Library.objects.all()
        context['recently_checked_out_books'] = Book.objects.filter(checkout_status=True)
        context['recently_checked_in_books'] = Book.objects.filter(checkout_status=False)
        context['recent_books'] = Book.objects.order_by('pub_date').reverse()[:5]
        return context

class AboutView(generic.TemplateView):
    template_name = 'Library/about.html'

class SystemBookView(generic.ListView):
    template_name = 'Library/system_books.html'
    context_object_name = 'book_list'
    
    def get_queryset(self):
        return Book.objects.order_by('title')

class LibraryBookView(generic.DetailView):
    model = Library 
    template_name = 'Library/library_books.html' 

class BookView(generic.DetailView):
    model = Book
    template_name = 'Library/faculty.html'

def checkout(request, book_id):
    return HttpResponse("Now checking out Book %s" % book_id)  
