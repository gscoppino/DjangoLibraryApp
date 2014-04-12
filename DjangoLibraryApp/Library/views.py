from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from Library.models import * 
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'Library/index.html'
    context_object_name = 'library_list'

    def get_queryset(self):
        return Library.objects.order_by('name')

class SystemBookView(generic.ListView):
    template_name = 'Library/system_books.html'
    context_object_name = 'book_list'
    
    def get_queryset(self):
        return Book.objects.order_by('title')

class DetailView(generic.DetailView):
    model = Library 
    template_name = 'Library/student_grade.html' #temp

def checkout(request, book_id):
    return HttpResponse("Now checking out Book %s" % book_id)  
