from django.shortcuts import render, redirect
from .models import Input
from .forms import InputForm


def home(request):
	inputs = Input.objects.order_by('-date_posted')

	context = {'inputs' : inputs}

	return render(request, 'inputs/home.html', context)

def input(request):
	
	if request.method == 'POST':

		form = InputForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = InputForm()

	context = {'form':form}

	return render(request, 'inputs/input.html', context)