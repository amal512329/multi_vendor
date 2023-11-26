from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import CreateVendor,Domain
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db import connection,router
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from products.models import Product
from user.models import CreateVendor

# Create your views here.

def index(request):

    return HttpResponse('This is The Admin Account ')



from django.shortcuts import render
from .models import CreateVendor
from products.models import Product

def vendor_products(request):
    # Fetch all vendors and their products
    vendors = CreateVendor.objects.all()
    vendor_products = []

    for vendor in vendors:
        products = Product.objects.filter(vendor=vendor)
        vendor_products.append({'vendor': vendor, 'products': products})

    return render(request, 'user/vendor_products.html', {'vendor_products': vendor_products})



def public_index(request):
    all_vendors = CreateVendor.objects.all()
    all_products = []

    # Skip the first vendor (public schema)
    for vendor in all_vendors[1:]:
        schema_name = vendor.schema_name

        # Connect to the vendor's schema
        with connection.cursor() as cursor:
            cursor.execute(f"SET search_path TO {schema_name}")

            # Fetch products for the vendor
            products_query = "SELECT product_name, description, price FROM products_product;"
            print(f"Query for {vendor.name}: {products_query}")
            cursor.execute(products_query)
            products = cursor.fetchall()
            print(products)

            # Add the products to the overall list
            all_products.extend(products)

    return render(request, 'public_index.html', {'all_products': all_products})