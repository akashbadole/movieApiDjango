from django.db import models

# Create your models here.
class Moviesdetail(models.Model):
    Name = models.CharField(max_length=255)
    Story  = models.CharField(max_length=255)
    Actor  = models.CharField(max_length=255)
    Genre  = models.CharField(max_length=255)
    Year   = models.CharField(max_length=255)
    Budget = models.CharField(max_length=255)
    BoxOfficeCollection = models.CharField(max_length=255)