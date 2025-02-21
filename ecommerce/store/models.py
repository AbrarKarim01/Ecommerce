from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True) # for category (see urls: /shoes/nike-air-jordan)

    class Meta:
        verbose_name_plural = 'categories' # overriding Categorys into categories

    # Shirt/Shoes instead of default value Category (1)/Category(2)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description =models.TextField(blank=True)
    slug = models.SlugField(max_length= 255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/') # install Pillow ((venv), ecommerce -> terminal: pip install Pillow) before this


    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
    
# (Creating models) for migration to db.sqlite3 ->in (venv) ecommerce python manage.py makemigrations
# When makemigrations is completed, it will be visible in the store (app) file -> migration -> 0001_initial.py
# then, use python manage.py migrate to migrate
# this migrate the admin, auth, contenttypes, sessions , store (located at settings.py under app)


