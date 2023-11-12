from django.shortcuts import render
from .forms import MyForm

def products(request):
    return render(request, 'products.html')