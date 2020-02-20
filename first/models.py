from django.db import models

class tips_calculator(models.Model):
    sub_total = models.FloatField()
    tax = models.FloatField()

    def total_amount(self):
        return self.sub_total + (self.sub_total *(self.tax/100))

    total_Cost = total_amount

class Books(models.Model):
    name = models.CharField(max_length= 50)
    author = models.CharField(max_length = 30, default='test')
    emil = models.EmailField(blank = True)
    describe = models.TextField(default = 'DataFlair Django tutorials')

    def __str__(self):
        return self.name

class test(models.Model):
    name = models.CharField(max_length = 100)
    

    def __str__(self):
        return self.name
