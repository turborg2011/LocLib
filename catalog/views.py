from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre

def index(request):
    """
    Func for home-page
    :param request:
    :return: home-page
    """
    #Count of some main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Count available books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    #тут либо object либо objects
    num_authors = Author.objects.count()

    num_books_found_edge = Book.objects.all().filter(title="Foundation's Edge").count()

    #Render HTML with given data inside variable 'context'
    return render(
        request, 'index.html',
        context={'num_books':num_books, 'num_instances':num_instances,
                 'num_instances_available':num_instances_available, 'num_authors': num_authors,
                 'num_books_found_edge':num_books_found_edge}
    )


from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book
