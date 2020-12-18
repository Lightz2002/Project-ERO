from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('edit/profile/', views.edit_profile, name='edit_profile'),
    path('change/password/', views.change_password, name='change_password'),
]
