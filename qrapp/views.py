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
        code_data=request.POST.get('scan-result')
        qr_code_scan=QRCodeData(data=code_data)
        qr_code_scan.save()
        messages.success(request, 'QR Code scanning data saved succefully!')
        return render(request,'success.html')
    return render(request,'scan.html')

def genView(request):
    return render(request,'add.html')