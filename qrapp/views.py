from django.shortcuts import render
from django.views import View
from .models import QRCodeData
# Create your views here.

def homeView(request):
    render(request,'index.html')

def searchView(request):
    qrcode_data=QRCodeData.objects.all()
    return render(request,'review.html',{'qrcode_data':qrcode_data})

def scanView(request):
    qrcode_data=QRCodeData.objects.all()
    return render(request,'review.html',{'qrcode_data':qrcode_data})

def genView(request):
    return render(request,'success.html')