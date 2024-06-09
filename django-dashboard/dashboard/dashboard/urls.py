# dashboard/urls.py
from django.contrib import admin
from django.urls import include, path
from dashboard_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard_app/', include('dashboard_app.urls')),
    path('', views.index, name='index'),
]
