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
def checkoutView(request):
    if request.method=='POST':
        scan_track=request.POST.get('result')
        try:
            entry=QRCodeData.objects.get(code_data=scan_track)
            entry.check_out=True
            entry.save()
            context={
                "message":"checkout successfully!"
            }
            return render(request,'message.html', context=context)
        except QRCodeData.DoesNotExist:
            context={
                "message":"checkout failed!"
            }
            return render(request,'message.html', context=context)
    return render(request,'checkout.html')

@login_required
def addView(request):
    return render(request,'add.html')

@login_required
def addscanView(request):
    if request.method=='POST':
        scan_track=request.POST.get('result')
        scan_receiver=request.POST.get('receiver')
        #compare existed query
        entry_exists=QRCodeData.objects.filter(code_data=scan_track).exists()
        if entry_exists:
            context={
                "message":"scanning result already exists!"
            }
        else:
            qr_code_scan=QRCodeData(receiver=scan_receiver, code_data=scan_track)
            qr_code_scan.save()
            context={
                "message":"add scanning successfully!"
            }
        return render(request,'message.html', context=context)
    return render(request,'add_scan.html')

@login_required
def addgenView(request):
    return render(request,'add_generate.html')