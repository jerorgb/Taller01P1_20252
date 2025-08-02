from django.shortcuts import render

from django.http import HttpResponse

from .models import Movie

def home(request):
    #return render(request, 'home.html')
    SearchTerm = request.GET.get('searchMovie')
    if SearchTerm:
        movies = Movie.objects.filter(title__icontains=SearchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})


def about(request):
    return render (request, 'about.html')

# Create your views here.
