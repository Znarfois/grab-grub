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
    customers = Customer.objects.all()
    return render(request, 'Kiosk/view_customer.html', { 'customers': customers })

def view_food(request):
    foods = Food.objects.all()
    return render(request, 'Kiosk/food_details.html', { "foods": foods })

def delete_food(request, pk):
    Food.objects.filter(pk=pk).delete()
    return redirect("view_food")

def delete_customer(request, pk):
    Customer.objects.filter(pk=pk).delete()
    return redirect("view_customer")

def delete_order(request, pk):
    Order.objects.filter(pk=pk).delete()
    return redirect("home")

def orderdetails(request, pk):
    if request.method == 'POST':
        qty = request.POST.get('qty')
        payment_mode = request.POST.get('payment_mode')
        Order.objects.filter(pk=pk).update(qty=qty, payment_mode=payment_mode)
        message = "Successfully updated."
        return redirect('orderdetails', pk=pk)

    orders = Order.objects.filter(pk=pk)
    return render(request, 'Kiosk/orderdetails.html', { "orders": orders })

def customer_details(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        Customer.objects.filter(pk=pk).update(name=name, address=address, city=city)
        message = "Successfully updated."
        return redirect('customer_details', pk=pk)

    customers = Customer.objects.filter(pk=pk)
    return render(request, 'Kiosk/customer_details.html', { "customers": customers })

def food_details(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        created_at = datetime.now()
        Food.objects.filter(pk=pk).update(name=name, description=description, price=price, created_at=created_at)
        message = "Successfully updated."
        return redirect('food_details', pk=pk)

    foods = Food.objects.filter(pk=pk)
    return render(request, 'Kiosk/food_details.html', { "foods": foods })
    
def addfood(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        created_at = datetime.now()

        Food.objects.create(name=name, description=description, price=price, created_at=created_at)
        food = Food.objects.all()
        return render(request, 'Kiosk/addfood.html', {'food': food})

    else:
        food = Food.objects.all()
        return render(request, 'Kiosk/addfood.html', {'food': food})
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
