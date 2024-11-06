from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request ,"index.html")

def intro(request):
    return render (request , "intro.html")

def about(request):
    return render (request, "about.html")