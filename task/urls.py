from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/',home),
    path('menu/',menu),
    path('about/',about),
]
