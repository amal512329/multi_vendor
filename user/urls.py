
from django.contrib import admin
from django.urls import include, path

from user.views import index,public_index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('user', public_index, name='public_index'),

 
]