from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required

# Create your views here.

def investor(request):
    print("hello world!")
    return render(request,"investor.html" )

    

# relative import of forms
#from .models import creator_Basic, creator_fund
#from .forms import creatorBasic


def investor_view(request):
	# dictionary for initial data with
	# field names as keys
	return render(request,"investor.html",)


	# add the dictionary during initialization
	
		
	
	return render(request, "investor_view.html", context)

class ProfileView(View):
    def get (self,request):
       return render(request, 'profile.html')