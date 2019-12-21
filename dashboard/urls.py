"""
    Dashboard URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('search', views.search, name="search"),
    path('cctv', views.cctv, name="cctv"),
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
]
