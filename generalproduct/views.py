from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Category,Product
 
def home(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.filter()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)
