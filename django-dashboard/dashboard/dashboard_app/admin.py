# dashboard_app/admin.py
from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItem, SalesReport

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(SalesReport)
