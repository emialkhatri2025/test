from django.db import models

class movies(models.Model):
    movie_name = models.CharField(max_length = 100)
    movie_actor = models.CharField(max_length = 100)
    movies_actress = models.CharField(max_length = 100)
    movie_released = models.DateField()


    def __str__(self):
        return self.movie_name

class movieType(models.Model):
    movie_generay = models.CharField(max_length = 25)
    movie_type = models.CharField(max_length = 20)
    movies = models.ManyToManyField(movies)

    def __str__(self):
        return self.movie_generay
