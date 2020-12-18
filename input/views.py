from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import InputForm,Input
from .filters import InputFilter
from login.views import logout

# Create your views here.
@login_required
def input(request):	
	data = Input.objects.all()

	Filter = InputFilter(request.GET, queryset=data)

	data = Filter.qs

	context = {
		'menu' : ['Input', 'Retur', 'Product', 'Setting'],
		'menu_name' : 'Input',		
		'page_title' : 'Input',
		'button_class' : 'create-button',
		'data' : data,
		'Filter' : Filter,
	}

	return render(request, 'input.html', context)

@login_required
def create_input(request):
	form = InputForm()
	if request.method == 'POST':	
		form = InputForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('input')

	context = {
		'menu' : ['Input', 'Retur', 'Product', 'Setting'],
		'menu_name' : 'Input (Create)',
		'page_title' : 'Input (Create)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'form' : form
	}

	return render(request, 'create_input.html', context)

@login_required
def update_input(request, pk):
	obj = Input.objects.get(id=pk)
	form = InputForm(instance=obj)

	if request.method == 'POST':
		form = InputForm(request.POST, instance=obj)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Input Data Has Been Updated')
			return redirect('input')

	context = {
		'menu' : ['Input','Retur', 'Product', 'Setting'],
		'menu_name' : 'Input (Update)',
		'page_title' : 'Input (Update)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'input' : obj,
		'form' : form,
	}

	return render(request, 'create_input.html', context)

@login_required
def delete_input(request, pk):
	data = Input.objects.all()

	obj = get_object_or_404(Input, id=pk)
	form = InputForm(instance=obj)


	if request.method == 'POST':
		obj.delete()
		messages.success(request, 'Your Data Has Been Deleted')
		return redirect('input')
		
	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Input (Delete)',
		'data' : data,
		'input' : obj,
		'form' : form,
	}

	return render(request, 'delete_input.html', context)
