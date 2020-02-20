from django.db import models

class Demployee(models.Model):
    name = models.CharField(max_length = 100)
    department = models.CharField(max_length= 20)
    role =  models.CharField(max_length = 50)
    salary = models.FloatField()

    def __str__(self):
        return self.name
