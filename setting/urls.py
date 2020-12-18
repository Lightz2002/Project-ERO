from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.setting, name='setting'),
    path('uom/', views.setting_uom, name='setting_uom'),
    path('uom/create', views.create_uom, name='create_uom'),
	path('uom/update/<int:pk>/', views.update_uom, name='update_uom'),
    path('uom/delete/<int:pk>/', views.delete_uom, name='delete_uom'),
    path('warehouse/', views.setting_warehouse, name='setting_warehouse'),
    path('warehouse/create', views.create_warehouse, name='create_warehouse'),
	path('warehouse/update/<int:pk>/', views.update_warehouse, name='update_warehouse'),
    path('warehouse/delete/<int:pk>/', views.delete_warehouse, name='delete_warehouse'),    
    path('supplier/', views.setting_supplier, name='setting_supplier'),
    path('supplier/create', views.create_supplier, name='create_supplier'),
    path('supplier/update/<int:pk>/', views.update_supplier, name='update_supplier'),
    path('supplier/delete/<int:pk>/', views.delete_supplier, name='delete_supplier'),
    path('category/', views.setting_category, name='setting_category'),
    path('category/create', views.create_category, name='create_category'),
    path('category/update/<int:pk>/', views.update_category, name='update_category'),
    path('category/delete/<int:pk>/', views.delete_category, name='delete_category'),
]












