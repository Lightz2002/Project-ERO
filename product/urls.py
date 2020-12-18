from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('create/', views.create_product, name='create_product'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
]












