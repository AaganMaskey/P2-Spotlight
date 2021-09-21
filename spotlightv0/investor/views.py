from django.shortcuts import render , redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .models import investor_fund
# Create your views here.

def investor(request):
    print("hello world!")
    return render(request,"investor.html" )



# relative import of forms
#from .models import creator_Basic, creator_fund
#from .forms import creatorBasic


#def InvestorCheckoutView(request):
	# dictionary for initial data with
	# field names as keys
#	class InvestorCheckoutView(View):
#		def get(self, request, id):
#				return render(request,"investor-checkout.html",)

def InvestorCheckoutView(request, pid):
    #projObj = creator_Basic.objects.get(pk=pid)
    return render(request, "investor-checkout.html")

def Add_Fund(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        
        amount = request.POST['pledgeAmount']
        
        try:
            investor_fund.objects.create(
                
                pledgeAmount=amount,
                
            )
            error = "no"
        except Exception as e:
            print(e)
            error = "yes"
    p = {'error': error}
    return render(request, 'investor-checkout.html', p)

