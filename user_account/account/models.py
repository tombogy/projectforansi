from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Driver(models.Model):
    name = models.CharField(max_length=100)
    mobile= models.CharField(max_length=15)
    license = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    did = models.CharField(max_length=10, unique=True)
    password= models.CharField(max_length=100)
    photo = models.ImageField(upload_to='driver_photos/')

    def __str__(self):
        return self.name

    
    