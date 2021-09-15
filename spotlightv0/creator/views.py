from django.shortcuts import render

# Create your views here.

def create(request):
    print("hello world!")
    return render(request,"create.html" )

    

# relative import of forms
from .models import creator_Basic, creator_fund
from .forms import creatorBasic


def create_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = GeeksForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "create_view.html", context)
