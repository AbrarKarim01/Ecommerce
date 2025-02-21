from django.contrib import admin

# Register your models here.
from . models import Category, Product

admin.site.register(Category)
admin.site.register(Product)

# for accessing the ADMIN Panel create super user by python manage.py createsuperuser