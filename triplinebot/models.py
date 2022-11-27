from django.db import models

class Location(models.Model):
    area = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)