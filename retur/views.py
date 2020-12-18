from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import ReturForm,Retur
from .filters import ReturFilter
from login.views import logout

# Create your views here.
@login_required
def retur(request):	
	data = Retur.objects.all()

	Filter = ReturFilter(request.GET, queryset=data)

	data = Filter.qs

	context = {
		'menu' : ['Input', 'Retur', 'Product', 'Setting'],
		'menu_name' : 'Retur',
		'page_title' : 'Retur',
		'button_class' : 'create-button',
		'data' : data,
		'Filter' : Filter,
	}

	return render(request, 'retur.html', context)

@login_required
def create_retur(request):
	form = ReturForm()
	if request.method == 'POST':	
		form = ReturForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('retur')

	context = {
		'menu' : ['Input', 'Retur', 'Product', 'Setting'],
		'menu_name' : 'Retur (Create)',
		'page_title' : 'Retur (Create)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'form' : form
	}

	return render(request, 'create_retur.html', context)

@login_required
def update_retur(request, pk):
	obj = Retur.objects.get(id=pk)
	form = ReturForm(instance=obj)

	if request.method == 'POST':
		form = ReturForm(request.POST, instance=obj)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Retur Data Has Been Updated')
			return redirect('retur')

	context = {
		'menu' : ['Input','Retur', 'Product', 'Setting'],
		'menu_name' : 'Retur (Update)',
		'page_title' : 'Retur (Update)',
		'button_class1' : 'save-button',
		'button_class2' : 'cancel-button',
		'retur' : obj,
		'form' : form,
	}

	return render(request, 'create_retur.html', context)

@login_required
def delete_retur(request, pk):
	data = Retur.objects.all()

	obj = get_object_or_404(Retur, id=pk)
	form = ReturForm(instance=obj)


	if request.method == 'POST':
		obj.delete()
		messages.success(request, 'Your Data Has Been Deleted')
		return redirect('retur')
		
	context = {
		'menu' : ['Input','Retur','Product', 'Setting'],
		'page_title' : 'Retur (Delete)',
		'data' : data,
		'retur' : obj,
		'form' : form,
	}

	return render(request, 'delete_retur.html', context)
