from .models import investor_fund
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from creator.models import creator_Basic
# Create your views here.


def investor(request):
    print("hello world!")
    return render(request, "investor.html")


# relative import of forms
# from .models import creator_Basic, creator_fund
# from .forms import creatorBasic


# def InvestorCheckoutView(request):
    # dictionary for initial data with
    # field names as keys
#	class InvestorCheckoutView(View):
#		def get(self, request, id):
#				return render(request,"investor-checkout.html",)

def InvestorCheckoutView(request, pid):
    projObj = creator_Basic.objects.get(pk=pid)
    data = creator_Basic.objects.all().order_by('-TargetLaunchDate')
    return render(request, "investor-checkout.html", {"fundProject": projObj, "projects": data})


def AddFund(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        amount = request.POST['amount']
        projectId = request.POST['projectId']
        userId = request.POST['userId']
        userName = request.POST['userName']

        try:
            investor_fund.objects.create(
                pledgeAmount=amount,
                userid=userId,
                username=userName,
                projectid=projectId
            )
            obj = creator_Basic.objects.get(pk=projectId)
            obj.pledgeAmount = obj.pledgeAmount + amount
            obj.save()

            error = "no"
        except Exception as e:
            print(e)
            error = "yes"
    p = {'error': error}
    return render(request, 'investor-checkout.html', p)
