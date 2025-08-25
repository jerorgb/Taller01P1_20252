from django.shortcuts import render
from django.http import HttpResponse

import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

from .models import Movie

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies, 'searchTerm': searchTerm})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})

def about(request):
    return render('about.html')

def statistics_view(request):
    matplotlib.use('Agg')  # Use a non-interactive backend
    all_movies = Movie.objects.all()
    movie_counts_per_year = {}
    for movie in all_movies:
        year = movie.year
        if year in movie_counts_per_year:
            movie_counts_per_year[year] += 1
        else:
            movie_counts_per_year[year] = 1
            
    bar_width = 0.4
    bar_positions = range(len(movie_counts_per_year))
    plt.bar(bar_positions, movie_counts_per_year.values(), width=bar_width, align='center')
    
    plt.title('Number of Movies Released Each Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(bar_positions, movie_counts_per_year.keys(), rotation=90)
    
    plt.subplots_adjust(bottom=0.2)
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    g1 = graphic.decode('utf-8')
    
    
    
    
    
    matplotlib.use('Agg')  # Use a non-interactive backend
    all_movies = Movie.objects.all()
    movie_counts_per_genre = {}
    for movie in all_movies:
        genre = movie.genre
        if genre in movie_counts_per_year:
            movie_counts_per_genre[genre] += 1
        else:
            movie_counts_per_genre[genre] = 1
            
    bar_width = 0.1
    bar_positions = range(len(movie_counts_per_genre))
    plt.bar(bar_positions, movie_counts_per_genre.values(), width=bar_width, align='center')
    
    plt.title('Number of Movies per genre')
    plt.xlabel('genre')
    plt.ylabel('Number of Movies')
    plt.xticks(bar_positions, movie_counts_per_genre.keys(), rotation=90)
    
    plt.subplots_adjust(bottom=0.6)
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    g2 = graphic.decode('utf-8')
    
    return render(request, 'statistics.html', {'g1': g1, 'g2': g2})
    