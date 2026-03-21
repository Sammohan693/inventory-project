from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('inventory/', views.inventory_page, name="inventory"),
    path('add/', views.add_product, name="add"),

    path('sales/', views.sales, name="sales"),
    path('purchases/', views.purchases, name="purchases"),
    path('reports/', views.reports, name="reports"),

    # 🔥 AUTH
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('product/<int:id>/', views.product_detail, name="product_detail"),
     
    path('create-admin/', views.create_admin, name="create_admin"),
]


