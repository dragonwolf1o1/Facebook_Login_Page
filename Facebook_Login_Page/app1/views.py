from django.shortcuts import render, HttpResponse
from .models import Login_Details

# Create your views here.
def index(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        submit=Login_Details(email=email,password=password)
        submit.save()
    return render(request,'index.html')