from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

#Page not found view
atype_list = ['cooperative', 'factory', 'fro', 'farmer', 'device', 'product']

def login(request):
	context = {}
	return render(request, 'KiloSahihi/login.html', context)

def recover(request):
	context = {}
	return render(request, 'KiloSahihi/recover.html', context)

# @login_required
def register(request, atype):
	if atype not in atype_list:
		return render(request, 'KiloSahihi/404.html')

	context = {}
	if atype == 'farmer':
		return render(request, 'KiloSahihi/register/farmer.html', context)
	elif atype == 'factory':
		return render(request, 'KiloSahihi/register/factory.html', context)
	elif atype == 'fro':
		return render(request, 'KiloSahihi/register/fro.html', context)
	elif atype == 'device':
		return render(request, 'KiloSahihi/register/device.html', context)
	elif atype == 'product':
		return render(request, 'KiloSahihi/register/product.html', context)
	else:
		return render(request, 'KiloSahihi/404.html', context)

def data_settings(request, atype, theid):
	if atype not in atype_list:
		return render(request, 'KiloSahihi/404.html')

	context = {}
	if atype == 'farmer':
		return render(request, 'KiloSahihi/settings/farmer.html', context)
	elif atype == 'factory':
		return render(request, 'KiloSahihi/settings/factory.html', context)
	elif atype == 'fro':
		return render(request, 'KiloSahihi/settings/fro.html', context)
	elif atype == 'device':
		return render(request, 'KiloSahihi/settings/device.html', context)
	elif atype == 'product':
		return render(request, 'KiloSahihi/settings/product.html', context)
	else:
		return render(request, 'KiloSahihi/404.html', context)

"""
def register_coopperative(request):
	context = {}
	return render(request, 'KiloSahihi/login.html', context)

def register_factory(request):
	context = {}
	return render(request, 'KiloSahihi/login.html', context)

def register_fro(request):
	context = {}
	return render(request, 'KiloSahihi/login.html', context)

def register_farmer(request):
	context = {}
	return render(request, 'KiloSahihi/login.html', context)
"""

# @login_required
def settings(request, atype):
	if atype not in atype_list:
		return render(request, 'KiloSahihi/404.html')

	context = {}
	return render(request, 'KiloSahihi/login.html', context)

"""
def settings_coopperative(request):
	context = {}
	return render(request, 'KiloSahihi/login.html', context)

def settings_factory(request):
	context = {}
	return render(request, 'KiloSahihi/login.html', context)

def settings_fro(request):
	context = {}
	return render(request, 'KiloSahihi/login.html', context)

def settings_farmer(request):
	context = {}
	return render(request, 'KiloSahihi/login.html', context)
"""

# @login_required
def home(request):
	context = {}
	return render(request, 'KiloSahihi/home.html', context)

def farmers(request):
	context = {}
	return render(request, 'KiloSahihi/farmers.html', context)

def factories(request):
	context = {}
	return render(request, 'KiloSahihi/factories.html', context)

def transactions(request):
	context = {}
	return render(request, 'KiloSahihi/transactions.html', context)

def fro(request):
	context = {}
	return render(request, 'KiloSahihi/fro.html', context)

def devices(request):
	context = {}
	return render(request, 'KiloSahihi/devices.html', context)

def products(request):
	context = {}
	return render(request, 'KiloSahihi/products.html', context)

def page_not_found(request):
	context = {}
	return render(request, 'KiloSahihi/404.html', context)
