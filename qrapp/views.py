from django.shortcuts import render
from django.views import View
from .models import QRCodeData
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
    return render(request,'scan.html')

def genView(request):
    return render(request,'add.html')