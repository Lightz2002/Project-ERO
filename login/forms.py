from django import forms 
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Account


class CreateUserForm(UserCreationForm):
	def __init__(self,*args):
		super().__init__(*args)
		self.label_suffix = ""
		
	company_name	= forms.CharField(max_length=255)
	city 			= forms.CharField(max_length=255)
	address			= forms.CharField(max_length=255) 
	email 			= forms.EmailField(max_length=50)

	class Meta():
		model = Account 
		fields = ('company_name','city','address','email','password1','password2')
		

class LoginForm(forms.ModelForm):
	def __init__(self,*args):
		super().__init__(*args)
		self.label_suffix = ""
		
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta():
		model = Account 
		fields = ('company_name','password')

	def clean(self):
		company_name = self.cleaned_data['company_name']
		password = self.cleaned_data['password']
		if not authenticate(company_name=company_name, password=password):
			raise forms.ValidationError('Company name or password is incorrect')