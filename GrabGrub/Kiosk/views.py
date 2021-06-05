from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from datetime import datetime

def login(request):
    message = ""

    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('password')
        if  User.objects.filter(username=un, password=pw).exists():
            message = ""
            return redirect('home')
        else: 
            # Used as an alternative to alerts
            message = "User unknown or incorrect password. Please try again."
        #     return render(request, 'Kiosk/login.html')
    return render(request, 'Kiosk/login.html', {'message': message})

def create_user(request):
    message = ""

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if  User.objects.filter(username=username).exists():
            message = "Account already exists"
        else: 
            # Used as an alternative to alerts
            message = "Account Successfully created."
            User.objects.create(username=username, password=password)
            return render(request, 'Kiosk/login.html')
    return render(request, 'Kiosk/create_user.html', {'message': message})

def home(request):
    orders = Order.objects.all()
    return render(request, 'Kiosk/home.html', { 'orders': orders })

def view_customer(request):
    return render(request, 'Kiosk/customer_details.html')

def view_food(request):
    return render(request, 'Kiosk/view_food.html')

def orderdetails(request):
    return render(request, 'Kiosk/orderdetails.html')

def addorder(request):

    if request.method == "POST":
        food_pk = request.POST.get("food")
        qty = request.POST.get("qty")
        date = request.POST.get("date")
        cust_pk = request.POST.get("cust")
        mode = request.POST.get("mode")

        food = Food.objects.get(pk=food_pk)
        cust = Customer.objects.get(pk=cust_pk)

        if date == "":
            date = datetime.now()
        Order.objects.create(food=food, ordered_at=date, cust_order=cust, payment_mode=mode, qty=qty)
        
        food = Food.objects.all()
        customers = Customer.objects.all()
        return render(request, 'Kiosk/addorder.html', {'food': food, 'customers':customers})

    else:
        food = Food.objects.all()
        customers = Customer.objects.all()
        return render(request, 'Kiosk/addorder.html', {'food': food, 'customers':customers})
