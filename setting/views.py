from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import *
from .models import *
# from .filters import UserFilter

# General Setting
@login_required
def setting(request):
	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting',
		'menu_name' : 'Setting',
	}

	return render(request, 'setting.html', context)

# UOM
@login_required
def setting_uom(request):
	data = Uom.objects.all()

	context = {
		'menu' : ['Input', 'Retur','Product', 'Setting'],
		'page_title' : 'Setting (Uom)',
		'menu_name' : 'Setting (Uom)',
		'button_class' : 'create-button',
		'data' : data
	}

	return render(request, 'uom/setting_uom.html', context)

@login_required
def create_uom(request):
	form = UomForm()

	if request.method == 'POST':
		form = UomForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('setting_uom')

	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting (Create Uom)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'form' : form
	}

	return render(request, 'uom/create_uom.html', context)

@login_required
def update_uom(request, pk):
	uom = Uom.objects.get(id=pk)
	form = UomForm(instance=uom)

	if request.method == 'POST':
		form = UomForm(request.POST, instance=uom)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Uom Data Has Been Updated')
			return redirect('setting_uom')

	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting (Update Uom)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'uom' : uom,
		'form' : form,
	}

	return render(request, 'uom/create_uom.html', context)

@login_required
def delete_uom(request, pk):
	data = Uom.objects.all()

	uom = get_object_or_404(Uom, id=pk)
	form = UomForm(instance=uom)

	if request.method == 'POST':
		uom.delete()
		messages.success(request, 'Your Data Has Been Deleted')
		return redirect('setting_uom')
		
	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting (Delete Uom)',
		'data' : data,
		'uom' : uom,
		'form' : form,
	}

	return render(request, 'uom/delete_uom.html', context)



# Warehouse
@login_required
def setting_warehouse(request):
	data = Warehouse.objects.all()

	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting (Warehouse)',
		'menu_name' : 'Setting (Warehouse)',
		'button_class' : 'create-button',
		'data' : data,
	}

	return render(request, 'warehouse/setting_warehouse.html', context)

@login_required
def create_warehouse(request):
	form = WarehouseForm()

	if request.method == 'POST':
		form = WarehouseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('setting_warehouse')

	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting (Create warehouse)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'form' : form
	}

	return render(request, 'warehouse/create_warehouse.html', context)

@login_required
def update_warehouse(request, pk):
	warehouse = Warehouse.objects.get(id=pk)
	form = WarehouseForm(instance=warehouse)

	if request.method == 'POST':
		form = WarehouseForm(request.POST, instance=warehouse)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Warehouse Data Has Been Updated')
			return redirect('setting_warehouse');

	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting (Update Warehouse)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'warehouse' : warehouse,
		'form' : form,
	}

	return render(request, 'warehouse/create_warehouse.html', context)

@login_required
def delete_warehouse(request, pk):
	data = Warehouse.objects.all()

	warehouse = get_object_or_404(Warehouse, id=pk)
	form =WarehouseForm(instance=warehouse)


	if request.method == 'POST':
		warehouse.delete()
		messages.success(request, 'Your Data Has Been Deleted')
		return redirect('setting_warehouse')
	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'menu_name' : 'Setting (Delete Warehouse)',
		'page_title' : 'Setting (Delete Warehouse)',
		'data' : data,
		'warehouse' : warehouse,
		'form' : form,
	}

	return render(request, 'warehouse/delete_warehouse.html', context)


# Supplier
@login_required
def setting_supplier(request):
	data = Supplier.objects.all()

	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting (Supplier)',
		'menu_name' : 'Setting (Supplier)',
		'button_class' : 'create-button',
		'data' : data,
	}

	return render(request, 'supplier/setting_supplier.html', context)

@login_required
def create_supplier(request):
	form = SupplierForm()

	if request.method == 'POST':
		form = SupplierForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('setting_supplier')

	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting (Create Supplier)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'form' : form,
	}

	return render(request, 'supplier/create_supplier.html', context)

@login_required
def update_supplier(request, pk):
	supplier = Supplier.objects.get(id=pk)
	form = SupplierForm(instance=supplier)

	if request.method == 'POST':
		form = SupplierForm(request.POST, instance=supplier)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Supplier Data Has Been Updated')
			return redirect('setting_supplier');

	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting (Update Supplier)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'supplier' : supplier,
		'form' : form,
	}

	return render(request, 'supplier/create_supplier.html', context)

@login_required
def delete_supplier(request, pk):
	data = Supplier.objects.all()

	supplier = get_object_or_404(Supplier, id=pk)
	form = SupplierForm(instance=supplier)


	if request.method == 'POST':
		supplier.delete()
		messages.success(request, 'Your Data Has Been Deleted')
		return redirect('setting_supplier')

	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'menu_name' : 'Setting (Delete Supplier)',
		'page_title' : 'Setting (Delete Supplier)',
		'data' : data,
		'supplier' : supplier,
		'form' : form,
	}

	return render(request, 'supplier/delete_supplier.html', context)



# Category
@login_required
def setting_category(request):
	data = Category.objects.all()

	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting (Category)',
		'menu_name' : 'Setting (Category)',
		'button_class' : 'create-button',
		'data' : data,
	}

	return render(request, 'category/setting_category.html', context)

@login_required
def create_category(request):
	form = CategoryForm()

	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('setting_category')

	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting (Create Category)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'form' : form,
	}

	return render(request, 'category/create_category.html', context)

@login_required
def update_category(request, pk):
	category = Category.objects.get(id=pk)
	form = CategoryForm(instance=category)

	if request.method == 'POST':
		form = CategoryForm(request.POST, instance=category)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Category Data Has Been Updated')
			return redirect('setting_category');

	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Setting (Update Category)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'category' : category,
		'form' : form,
	}

	return render(request, 'category/create_category.html', context)

@login_required
def delete_category(request, pk):
	data = Category.objects.all()

	category = get_object_or_404(Category, id=pk)
	form = CategoryForm(instance=category)


	if request.method == 'POST':
		category.delete()
		messages.success(request, 'Your Data Has Been Deleted')
		return redirect('setting_category')
		
	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'menu_name' : 'Setting (Delete Category)',
		'page_title' : 'Setting (Delete Category)',
		'data' : data,
		'category' : category,
		'form' : form,
	}

	return render(request, 'category/delete_category.html', context)

