from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jan(request):
    return HttpResponse("Set up and plan your goals ")

def feb(request):
    return HttpResponse("visit to a nice place")