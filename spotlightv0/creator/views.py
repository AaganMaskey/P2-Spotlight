from django.shortcuts import render

# Create your views here.

def create(request):
    print("hello world!")
    return render(request,"create.html" )
