from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.



PRODUCT_PLANS=(("nutrition","Nutrition plan"),("gym","Gym plan"))
class Product(models.Model):
    categary = models.CharField( max_length=50,choices=PRODUCT_PLANS,default="nutrition")
    name = models.CharField( max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    imageurl = models.TextField()
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name       

        
    
class Content(models.Model):
    product = models.OneToOneField(Product, on_delete = models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text




class Subscription(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete = models.CASCADE)
    created_at= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product
