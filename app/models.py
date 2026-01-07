from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=14, decimal_places=2)