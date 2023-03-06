from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def macha(request):
    return HttpResponse('<marquee><h1>vadhu le macha</h1></marquee>')

def ballaya(request):
    return HttpResponse('<marquee><h1>arey saale, kya re howle</marquee></h1>')