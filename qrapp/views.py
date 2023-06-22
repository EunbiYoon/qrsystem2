from django.shortcuts import render
from django.views import View
from .models import QRCodeData
from django.contrib import messages
from django.views.generic import TemplateView, ListView
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
        scan_code=request.POST.get('scanned_data')
        print("Scan_code "+str(scan_code))
        qr_code_scan=QRCodeData(code_data=scan_code)
        qr_code_scan.save()
        return render(request,'success.html', {'sucess_message':'QR code scanning data saves successfully'})
    return render(request,'scan.html')

def genView(request):
    return render(request,'add.html')

def successView(request):
    return render(request,'success.html')