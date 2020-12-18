from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required



from .forms import EditProfileForm
# Create your views here.
@login_required
def edit_profile(request):		
	form = EditProfileForm(instance=request.user)
	
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			messages.success(request, 'Your Profile Data Has Been Changed')
			return redirect('input')
			
	context = {
		'menu' : ['Input','Retur','Product', 'Setting', 'Help'],
		'page_title' : 'Change Account Profile',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'form' : form,
	}

	return render(request,'edit_profile.html',context)

@login_required
def change_password(request):
	form = SetPasswordForm(user=request.user)
	
	if request.method == 'POST':
		form = SetPasswordForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			messages.success(request, 'Your Password Has Been Changed')
			return redirect('input')
			
	context = {
		'menu' : ['Input','Retur','Product', 'Setting', 'Help'],
		'page_title' : 'Change Password',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'form' : form,
	}

	return render(request,'change_password.html',context)