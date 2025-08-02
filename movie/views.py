from django.shortcuts import render
from .models import Movie

from django.http import HttpResponse

from .models import Movie

def home(request):
<<<<<<< HEAD
    
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
        return render(request, 'home.html', {'movies': movies, 'searchTerm': searchTerm})
    
=======
    #return render(request, 'home.html')
    SearchTerm = request.GET.get('searchMovie')
    if SearchTerm:
        movies = Movie.objects.filter(title__icontains=SearchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

>>>>>>> development

def about(request):
    return render (request, 'about.html')

# Create your views here.
