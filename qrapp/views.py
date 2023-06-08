from django.shortcuts import render
from django.views import View
from .models import QRCodeData
# Create your views here.

def homeView(request):
    return render(request,'index.html')

def searchView(request):
    return render(request,'search.html')

def scanView(request):
    return render(request,'scan.html')

def genView(request):
    return render(request,'add.html')