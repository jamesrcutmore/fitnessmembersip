from django.contrib import admin
from .models import Product,Subscription,Content



# Register your models here.
admin.site.register(Subscription)
admin.site.register(Product)
admin.site.register(Content)