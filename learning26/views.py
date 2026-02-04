from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Jay Shree Ram")

def contact(request):
    return render(request,"contact.html")

def home(request):
    return render(request,"home.html")

def aboutUs(request):
    data = {"tname":"RCB","cap":"Rajat Patidar","tro":1} 
    return render(request,"about.html",data)