from django.db import models
from user.models import CreateVendor


class Product(models.Model):
    
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
 