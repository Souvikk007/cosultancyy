"""
URL configuration for ecommerce_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ecommerce_app.views import (
    index, service, contact, reviews, shop
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('service/', service, name='service'),
    path('contact/', contact, name='contact'),
    path('reviews/', reviews, name='reviews'),
    path('shop/', shop, name='shop'),
    path('index.html', index, name='index'),
    path('service.html', service, name='service'),
    path('contact.html', contact, name='contact'),
    path('reviews.html', reviews, name='reviews'),
    path('shop.html', shop, name='shop'),
    
    
]