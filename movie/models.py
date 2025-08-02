from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

def __str__(self):
    return self.title

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movies/images/')
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    url = models.URLField(blank=True)
    