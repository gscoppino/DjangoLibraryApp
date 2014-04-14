from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views import generic

from Library.models import * 
# Create your views here.
class IndexView(generic.ListView):
    model = Library 
    template_name = 'Library/index.html'
    context_object_name = 'home_data'

    def get_context_data(self, **kwargs):
        time = timezone.now()
        context = super(IndexView, self).get_context_data(**kwargs)
        context['library_list'] = Library.objects.all()
        context['recently_checked_out_books'] = Book.objects.filter(checkout_status=True)
        context['recently_checked_in_books'] = Book.objects.filter(checkout_status=False)
        context['recent_books'] = Book.objects.filter(pub_date__lte=time).order_by('pub_date').reverse()[:5]
        return context

class AboutView(generic.TemplateView):
    template_name = 'Library/about.html'

class SystemBookView(generic.ListView):
    template_name = 'Library/system_books.html'
    context_object_name = 'book_list'
    
    def get_queryset(self):
        return Book.objects.filter(pub_date__lte=timezone.now()).order_by('title')

class LibraryBookView(generic.DetailView):
    model = Library 
    template_name = 'Library/library_books.html' 

class BookView(generic.DetailView):
    model = Book
    template_name = 'Library/book.html'

def checkout_or_return(request, book_id):
    try:
        user = User.objects.get(username=request.user)
        book = Book.objects.get(id=book_id)
        if (book.checkout_client == user):
            book.checkout_client = None
            book.checkout_status = False
        else:
            book.checkout_client = user 
            book.checkout_status = True
        book.save()
        return HttpResponseRedirect('/') 
    except:
        return HttpResponse("wut")
