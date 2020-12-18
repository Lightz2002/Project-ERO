from django import forms
from .models import Input

class DateInput(forms.DateInput):
	input_type = 'date'

class InputForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.label_suffix = ""

	class Meta:
		model = Input
		fields = '__all__'
		labels = {
			'document_name' : 'Document name :', 
			'date' : 'Date :',
			'warehouse_name' : 'Warehouse name :',
			'supplier_name' : 'Supplier name :',
			'uom' : 'UOM',
			'product_name' : 'Product',
			'product_price' : 'Price'
		}
		widgets = {
			'date' : DateInput(),
		}
