from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product

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


# 🔷 ADD PRODUCT
def add_product(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            quantity=request.POST.get('quantity'),
            image=request.FILES.get('image')
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


# 🔥 REGISTER (CREATE ADMIN)
def register_view(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = User.objects.create_user(
                username=username,
                password=password
            )

            # 🔥 make admin
            user.is_staff = True
            user.is_superuser = True
            user.save()

            return redirect('login')

    return render(request, 'register.html')


# 🔥 LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

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


# 🔥 CREATE ADMIN (DIRECT URL)
def create_admin(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    user, created = User.objects.get_or_create(username="admin")

    user.set_password("admin123")
    user.is_staff = True
    user.is_superuser = True
    user.save()

    return HttpResponse("Admin created successfully")

