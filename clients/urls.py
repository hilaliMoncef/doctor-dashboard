from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="clients"),
    path('add', views.add, name="add_client"),
    path('edit/<int:id>', views.edit, name="edit_client"),
    path('delete/<int:id>', views.delete, name="delete_client")
]