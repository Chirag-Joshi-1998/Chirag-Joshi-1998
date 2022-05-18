from django.db import models

# Create your models here.
class Eductor(models.Model):
 name = models.CharField(max_length=50)
 number = models.CharField(max_length=50)
 city = models.CharField(max_length=50)