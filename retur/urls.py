from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.retur, name='retur'),
    path('update/<int:pk>/', views.update_retur, name='update_retur'),
    path('create/', views.create_retur, name='create_retur'),
    path('delete/<int:pk>/', views.delete_retur, name='delete_retur'),
]
