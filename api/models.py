from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2 , max_digits=100 )
    sale_price  = models.DecimalField(decimal_places=2 , max_digits=100 , null=True , blank=True)
    image = models.CharField(max_length=120,blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
