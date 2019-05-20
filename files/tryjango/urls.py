"""tryjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view
from pages.views import citaact,about_view

# from products.views import product_detail_view , product_create_view,render_initial_data
from products.views import render_initial_data,dynamic_lookup_view
from products.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('contact/',citaact,name='cuntact'),
    path('about/',about_view,name = 'about'),
    #path('create/',product_create_view,name = 'create'),
    path('create/',render_initial_data,name = 'create'),
    # path('product/',product_detail_view,name='product'),
    path('product/',render_initial_data,name='product'),
    path('product/<int:my_id>/',dynamic_lookup_view,name='product'),
    path('product/<int:my_id>/delete/',product_dele_view,name = 'product-delete')

]