from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def create(request):
    print("hello world!")
    return render(request,"create.html" )

    

# relative import of forms
from .models import creator_Basic, creator_fund
from .forms import creatorBasic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@require_POST
@csrf_exempt

def create_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = creatorBasic(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "create_view.html", context)

class ProfileView(View):
    def get (self,request):
       return render(request, 'profile.html')


#def addCreator(request):
 #   if request.method == "POST":
  #   creator_Basic.objects.all()
   # creator_Basic.save()
    #return HttpResponseRedirect(reverse("view", args=(id,)))

def Add_Creator(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        name = request.POST['pname']  # The name mentioned in the text box should be mentioned here
        desc = request.POST['pdesc']
        cat = request.POST['category']
        try:
            creator_Basic.objects.create(
                title=name,
                description = desc,
                category = cat,
            
            )
            error = "no"
        except Exception as e:
            print(e)
            error = "yes"
    p = {'error': error}
    return render(request, 'create.html', p)    

def View_Projects(request):
    if not request.user.is_authenticated:
        return redirect('login')
    create = creator_Basic.objects.all()
    c = {'create': create}
    return render(request, 'view_created_projects.html', c)