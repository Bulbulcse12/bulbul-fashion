from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from django.urls import reverse



def home_page(request):
    products = Product.objects.all().filter(is_available=True)
    
    contex = {
        'products': products,
    }
    return render(request,'home.html',contex)