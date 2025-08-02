from django.shortcuts import render
from .models import Movie

from django.http import HttpResponse

def home(request):
    
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
        return render(request, 'home.html', {'movies': movies, 'searchTerm': searchTerm})
    

def about(request):
    return render (request, 'about.html')

# Create your views here.
