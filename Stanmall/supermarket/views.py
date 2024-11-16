from django.shortcuts import render

# Create your views here.
def index(request):
      return render(request,'home.html')

def insert(request):
      return render(request,'insert.html')