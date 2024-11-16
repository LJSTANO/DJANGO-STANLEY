from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Product

# Create your views here.

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def insert_data(request):

    if request.method == 'POST':
        prod_name = request.POST['prod_name']
        prod_price = request.POST['prod_price']
        prod_exp = request.POST['prod_exp']
        prod_quantity = request.POST['prod_quantity']
        prod_manufacture = request.POST['prod_manufacture']
        prod_description = request.POST['prod_description']
        prod_img = request.FILES['prod_img']

        # Create a new product object
        product = Product(
            prod_name=prod_name,
            prod_description=prod_description,
            prod_price=prod_price,
            prod_quantity=prod_quantity,
            prod_manufacture=prod_manufacture,
            prod_exp=prod_exp,
            prod_img=prod_img  # Use prod_img directly, no need for product.img
        )

        product.save()
        return redirect('/')

        return render(request, 'services.html')

def view (request):
    products = Product.objects.all()
    return render(request,'data.html',context={'products':products})

