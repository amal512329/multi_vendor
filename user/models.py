from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_tenants.models import DomainMixin,TenantMixin
from django.contrib.auth.models import User


# Create your models here.


class CreateVendor(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    # Add other fields as needed for the vendor model

    



class Domain(DomainMixin):
    pass