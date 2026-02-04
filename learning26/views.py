from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Jay Shree Ram")

def AboutUs(request):
    return render(request,"test.html")