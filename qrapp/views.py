from django.shortcuts import render
from django.views import View
from .models import QRCodeData
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse
# Create your views here.

class homeView(TemplateView):
    template_name='index.html'

class searchView(ListView):
    template_name='search.html'
    context_object_name='item_list'
    def get_queryset(self):
        return QRCodeData.objects.all()

def scanView(request):
    if request.method=='POST':
        scan_track=request.POST.get('result')
        scan_receiver=request.POST.get('receiver')
        qr_code_scan=QRCodeData(receiver=scan_receiver, code_data=scan_track)
        qr_code_scan.save()
        return render(request,'success.html', {'sucess_message':'QR code scanning data saves successfully'})
    return render(request,'scan.html')

def genView(request):
    return render(request,'add.html')

def checkoutView(request):
    if request.method=='POST':
        scan_track=request.POST.get('result')
        try:
            entry=QRCodeData.objects.get(code_data=scan_track)
            entry.check_out=True
            entry.save()
            return JsonResponse({'message':'Status Changed Successfully'})
        except QRCodeData.DoesNotExist:
            return JsonResponse({'message':'No mathcing entry found.'}, status=404)
    return render(request,'checkout.html')

def successView(request):
    return render(request,'success.html')