from django import forms
from login.models import Account

class EditProfileForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ('company_name','city','address','email')
