from django.shortcuts import render
from .models import people
from .models import products

# Create your views here.
def home(request):
    context = {}
    return render(request, 'websitedynamic/home.html', context)

def peoplelist(request):
    context = {}
    context['peoples'] = people.objects.all()
    return render(request, 'websitedynamic/people.html', context)

def productslist(request):
    context = {}
    context['productss'] = products.objects.all()
    return render(request, 'websitedynamic/products.html', context)
    
    
def contactus(request):
    context = {}
    return render(request, 'websitedynamic/contactus.html', context)



