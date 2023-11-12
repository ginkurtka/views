from django.urls import path
from .views import my_view
from .views1 import products

urlpatterns = [
    path('hello/', my_view),
    path('products/', products),
]