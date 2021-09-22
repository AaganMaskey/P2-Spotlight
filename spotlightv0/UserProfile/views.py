from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import creator_Basic
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def create(request):
    print("hello world!")
    return render(request, "create.html")


# relative import of forms


@require_POST
@csrf_exempt


class ProfileView(View):
    def get(self, request, username):
        return render(request, 'profile.html')


def Add_Profile(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        #name = request.creator.Auth
        usen = request.user.username
        eml = request.user.email
        ph = request.POST['phone']
        addr = request.POST['address']
        funded = request.investor.pledgeAmount
        proN = request.creator.title

        try:
            creator_Basic.objects.create(
                UserName = usen,
                Email = eml,
                Phone = ph,
                Address = addr,
                Funded = funded,
                Project = proN
            )
            error = "no"
        except Exception as e:
            print(e)
            error = "yes"
    p = {'error': error}
    return render(request, 'profile.html', p)


def View_Projects(request):
    # if not request.user.is_authenticated:
    #   return redirect('login')

    # data = creator_Basic.objects.all()
    data = creator_Basic.objects.all().order_by('-TargetLaunchDate')
    # paginator = Paginator(data, 9)
    return render(request, "home.html", {"projects": data})



def View_Projects_Details(request, pid):
    projObj = creator_Basic.objects.get(pk=pid)
    projLists = creator_Basic.objects.all()
    return render(request, "view-project-details.html", {"details": projObj, "projects": projLists})



def Projects_view(request):
    data = creator_Basic.objects.all().order_by('-TargetLaunchDate')
    return render(request, "view_all_projects.html", {"projects": data})


