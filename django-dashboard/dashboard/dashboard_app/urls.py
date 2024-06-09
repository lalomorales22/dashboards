# dashboard_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    path('analytics/', views.analytics, name='analytics'),
    path('settings/', views.settings, name='settings'),
    path('add_product/', views.add_product, name='add_product'),
    path('profile_settings/', views.profile_settings, name='profile_settings'),
    path('change_password/', views.change_password, name='change_password'),
    path('notification_settings/', views.notification_settings, name='notification_settings'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
