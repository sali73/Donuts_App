from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2 , max_digits=100 )
    sale_price  = models.DecimalField(decimal_places=2 , max_digits=100 , null=True , blank=True)
    image = models.CharField(max_length=120,blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    qty = models.DecimalField(decimal_places=2 , max_digits=100 , null=True)
    timestamp = models.DateTimeField(auto_now_add=True , null=True)
    update = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    def get_price(self):
        return self.price

class Cart(models.Model):
    products = models.ManyToManyField(Product,blank=True)
    totle = models.DecimalField(decimal_places=2 , max_digits=100 , default = 0.00 )
    active= models.BooleanField(default=True)

    def __unicode__(self):
        return "Cart id: %s " %(self.id)