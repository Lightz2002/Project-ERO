from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.input, name='input'),
    path('update/<int:pk>/', views.update_input, name='update_input'),
    path('create/', views.create_input, name='create_input'),
    path('delete/<int:pk>/', views.delete_input, name='delete_input'),
]
