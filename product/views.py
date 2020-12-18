from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import ProductForm,Product
from .filters import ProductFilter


@login_required
def product(request):
	data = Product.objects.all()

	Filter = ProductFilter(request.GET, queryset=data)

	data = Filter.qs

	context = {
		'menu' : ['Input', 'Retur', 'Product', 'Setting'],
		'page_title' : 'Product',
		'menu_name' : 'Product',
		'button_class' : 'create-button',
		'data' : data,
		'Filter' : Filter
	}

	return render(request, 'product.html', context)

@login_required
def create_product(request):
	form = ProductForm()

	if request.method == 'POST':
		form = ProductForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('product')
			
	context = {
		'menu' : ['Input', 'Retur', 'Product', 'Setting'],
		'page_title' : 'Product (Create)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'form' : form
	}

	return render(request, 'product_create.html', context)

@login_required
def update_product(request, pk):
	product = Product.objects.get(id=pk)
	form = ProductForm(instance=product)

	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES, instance=product)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Product Data Has Been Updated')
			return redirect('product')

	context = {
		'menu' : ['Input','Retur', 'Product', 'Setting'],
		'page_title' : 'Product (Update)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'product' : product,
		'form' : form,
	}

	return render(request, 'product_update.html', context)