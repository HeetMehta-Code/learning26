from django.http import HttpResponse
from django.shortcuts import render
from .models import User

def test1(request):
    return HttpResponse("StudentName: Paurav Patel")

def test2(request):
    return HttpResponse("Age: 28")

def test3(request):
    return HttpResponse("Profile: Business")

def contact(request):
    return render(request,"contact.html")

def home(request):
    return render(request,"home.html")

def aboutUs(request):
    data = {"tname":"RCB","cap":"Rajat Patidar","tro":1} 
    return render(request,"about.html",data)

def stu(request):
    cus = User.objects.all().values()
    print(cus)
    return HttpResponse("User data printed in terminal")
