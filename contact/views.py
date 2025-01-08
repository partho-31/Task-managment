from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def contact(request):
    return HttpResponse("<h1 style='color: red'>Patho Mobile  +8801865-815125.</h1>")