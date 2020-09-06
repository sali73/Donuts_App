from django.shortcuts import render
from .models import Product

# Create your views here.
def Index(request):
    product = [*Product.objects.all()]
    print(Product)
    return render(request,'product/Index.html' , {"Product": product})