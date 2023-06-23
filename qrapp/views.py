from typing import Any
from django.shortcuts import render
from django.views import View
from .models import QRCodeData
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

class homeView(TemplateView):
    template_name='home.html'

@login_required
def searchView(request):
    item_list=QRCodeData.objects.all()
    username=request.user.username
    context={
        'item_list':item_list,
        'username':username
    }
    return render(request, 'search.html', context)

@login_required
def scanView(request):
    if request.method=='POST':
        scan_track=request.POST.get('result')
        scan_receiver=request.POST.get('receiver')
        qr_code_scan=QRCodeData(receiver=scan_receiver, code_data=scan_track)
        qr_code_scan.save()
        return render(request,'success.html', {'sucess_message':'QR code scanning data saves successfully'})
    return render(request,'scan.html')

@login_required
def checkoutView(request):
    if request.method=='POST':
        scan_track=request.POST.get('result')
        try:
            entry=QRCodeData.objects.get(code_data=scan_track)
            entry.check_out=True
            entry.save()
            return render(request,'checkout_success.html')
        except QRCodeData.DoesNotExist:
            return render(request,'checkout_fail.html')
    return render(request,'checkout.html')

@login_required
def successView(request):
    return render(request,'success.html')

@login_required
def genView(request):
    return render(request,'generate.html')
