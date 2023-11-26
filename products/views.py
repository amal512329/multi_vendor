from django.shortcuts import render,redirect
from .models import Product
from user.models import CreateVendor
from django.db import connections


def index(request):
    products = Product.objects.all()
    return render(request,'client_index.html',{'products':products})
    


# Create your views here.
def create_product(request):
    if request.POST:
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        product = Product(product_name=product_name,description=description,price=price)
        product.save()
        return redirect('client_index')

   

    if request.POST:
        name = request.POST.get("name")
        employee = Employee(name=name)
        employee.save()
        return redirect('client_index')
    
