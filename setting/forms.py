from django import forms
from .models import *

class UomForm(forms.ModelForm):
	class Meta:
		model = Uom
		fields = '__all__'
		

class WarehouseForm(forms.ModelForm):
	class Meta:
		model = Warehouse
		fields = '__all__'
		

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'
		

class SupplierForm(forms.ModelForm):
	class Meta:
		model = Supplier
		fields = '__all__'
		


