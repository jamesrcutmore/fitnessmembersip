from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Member(models.Model):
    firstname = models.CharField( max_length=50)
    lastname = models.CharField( max_length=50)
    age = models.CharField( max_length=3)
    email = models.CharField( max_length=30)
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.firstname

PRODUCT_PLANS=(("nutrition","Nutrition plan"),("gym","Gym plan"))
class Product(models.Model):
    categary = models.CharField( max_length=50,choices=PRODUCT_PLANS,default="nutrition")
    name = models.CharField( max_length=50)
    imageurl = models.TextField()
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name       

        
    
