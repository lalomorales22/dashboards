# dashboard_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import ProductForm
from .models import Product, SalesReport, Order

def index(request):
    products = Product.objects.all()
    data = {
        'title': 'Dashboard',
        'cards': [
            {'title': 'Total Products', 'value': products.count(), 'description': 'Total number of products'},
            # Add more cards as needed
        ],
        'products': products
    }
    return render(request, 'dashboard_app/dashboard.html', data)

def reports(request):
    reports_data = SalesReport.objects.all()
    return render(request, 'dashboard_app/reports.html', {'title': 'Reports', 'reports': reports_data})

def analytics(request):
    total_orders = Order.objects.count()
    total_revenue = sum(order.total_amount for order in Order.objects.all())
    avg_order_value = total_revenue / total_orders if total_orders else 0
    monthly_sales = SalesReport.objects.all()[:6]  # Example data for the last 6 months

    data = {
        'title': 'Analytics',
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'avg_order_value': avg_order_value,
        'monthly_sales': monthly_sales
    }
    return render(request, 'dashboard_app/analytics.html', data)

def settings(request):
    return render(request, 'dashboard_app/settings.html', {'title': 'Settings'})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'dashboard_app/add_product.html', {'form': form})

def profile_settings(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        messages.success(request, 'Profile updated successfully')
    return redirect('settings')

def change_password(request):
    if request.method == 'POST':
        user = request.user
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password and user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Password changed successfully')
        else:
            messages.error(request, 'Password change failed')
    return redirect('settings')

def notification_settings(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.email_notifications = 'email_notifications' in request.POST
        profile.sms_notifications = 'sms_notifications' in request.POST
        profile.save()
        messages.success(request, 'Notification preferences updated successfully')
    return redirect('settings')

def delete_account(request):
    if request.method == 'POST':
        confirm_delete = request.POST['confirm_delete']
        if confirm_delete == 'DELETE':
            request.user.delete()
            messages.success(request, 'Account deleted successfully')
            return redirect('index')  # Or redirect to a goodbye page
        else:
            messages.error(request, 'Account deletion failed')
    return redirect('settings')
