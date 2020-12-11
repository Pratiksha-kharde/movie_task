from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class GenreData(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    imdb_score = models.DecimalField(max_digits=4, decimal_places=1)
    popularity_99 = models.DecimalField(max_digits=4, decimal_places=1)
    genre = models.ManyToManyField(GenreData)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name      
        
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    role_name = models.CharField(max_length=20)
    role_prev = models.IntegerField()
    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user
