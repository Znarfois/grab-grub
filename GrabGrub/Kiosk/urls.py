"""GrabGrub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('customers', views.view_customer, name='view_customer'),
    path('customer_details/<int:pk>', views.customer_details, name='customer_details'),
    path('orderdetails/<int:pk>', views.orderdetails, name='orderdetails'),
    path('addorder', views.addorder, name='addorder'),
    path('addfood', views.addfood, name='addfood'),
    path('create_user', views.create_user, name="create_user"),
    path('food_items', views.view_food, name="view_food"),
    path('food_details/<int:pk>', views.food_details, name="food_details"),
    path('delete_food/<int:pk>/', views.delete_food, name="delete_food"),
    path('delete_customer/<int:pk>/', views.delete_customer, name="delete_customer"),
    path('delete_order/<int:pk>/', views.delete_order, name="delete_order"),
]
