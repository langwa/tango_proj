from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    index_str = '<p>Rango says hello there world!</p> \
                 <p><a href=\'about\'>About</a></p>'
    return HttpResponse(index_str)

def about(request):
    about_str = '<p>Rango says here is the about page.</p> \
                 <p><a href=\'..\'>Home</a></p>'
    return HttpResponse(about_str)
