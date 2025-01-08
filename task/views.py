from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("This is Parth.") 

def menu(request):
    return HttpResponse("This is a menu.") 

def about(request):
    return HttpResponse("Let know about us.")