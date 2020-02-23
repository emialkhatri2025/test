from django.db import models

class movies(models.Model):
    movie_name = models.CharField(max_length = 100)
    movie_released = models.DateField()
    movie_generay = models.CharField(max_length = 25)
    movie_type = models.CharField(max_length = 20)

    def __str__(self):
        return self.movie_name
