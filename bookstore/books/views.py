from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model=Book
    context_object_name='book_list'
    template_name='book/book_list.html'

class BookDetailView(DetailView):
    model=Book
    template_name='books/book_detail.html'
