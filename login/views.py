from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import CreateUserForm,LoginForm

# Create your views here
def login_user(request):
	user = request.user
		
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			company_name = request.POST['company_name']
			password = request.POST['password']
			user = authenticate(company_name=company_name, password=password)
			if user:
				login(request,user)
				return redirect('input')

	context = {
		'page_title' : 'Login User',
		'title' : 'All In One Data Entry',
		'subtitle' : 'Login User',
		'destination' : 'regitration_admin',
		'login_form': form,
	} 

	return render(request, 'login_user.html', context, )


def register_user(request):
	form = CreateUserForm()
	if request.method == 'POST' :
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			company_name = form.cleaned_data.get('company_name')
			city = form.cleaned_data.get('city')
			address = form.cleaned_data.get('address')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password1')
			account = authenticate(company_name=company_name, city=city,address=address,email=email,password=password)
			messages.success(request, 'Account has been created for ' + company_name)
			login(request,account)
			return redirect('login_user')


	context = {
		'page_title' : 'Register User',
		'title' : 'All In One Data Entry',
		'subtitle' : 'Register User',
		'registration_form' : form,
	}


	return render(request, 'register_user.html', context)

@login_required
def logout(request):
	django_logout(request)
	return redirect('login_user')