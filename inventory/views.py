from django.shortcuts import render, redirect
from .models import Product

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# 🔷 HOME
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


# 🔷 INVENTORY
def inventory_page(request):
    products = Product.objects.all()

    total_products = products.count()
    low_stock = products.filter(quantity__lt=5).count()

    return render(request, 'inventory.html', {
        'products': products,
        'total_products': total_products,
        'low_stock': low_stock
    })


# 🔷 ADD PRODUCT (🔥 FIXED IMAGE)
def add_product(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST['name'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
            image=request.FILES['image']   # 🔥 IMPORTANT FIX
        )
        return redirect('inventory')

    return render(request, 'add.html')


# 🔷 SALES
def sales(request):
    return render(request, 'sales.html')


# 🔷 PURCHASES
def purchases(request):
    return render(request, 'purchases.html')


# 🔷 REPORTS
def reports(request):
    return render(request, 'reports.html')


# 🔥 REGISTER
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'register.html')


# 🔥 LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


# 🔥 LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')


# 🔷 PRODUCT DETAIL
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})

def inventory_page(request):
    products = Product.objects.all()

    total_products = products.count()
    low_stock = products.filter(quantity__lt=5).count()

    return render(request, 'inventory.html', {
        'products': products,
        'total_products': total_products,
        'low_stock': low_stock
    })
    
    