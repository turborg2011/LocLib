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

    #Render HTML with given data inside variable 'context'
    return render(
        request, 'index.html',
        context={'num_books':num_books, 'num_instances':num_instances,
                 'num_instances_available':num_instances_available, 'num_authors': num_authors}
    )



