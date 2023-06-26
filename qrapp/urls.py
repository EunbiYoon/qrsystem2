from django.urls import path
from .views import homeView,searchView,scanView,addView,successView, checkoutView, genView

urlpatterns = [
    path('',homeView.as_view(),name='home_url'),
    path('search',searchView, name='search_url'),
    path('checkout',checkoutView,name="checkout_url"),
    path('success',successView,name='success_url'),
    path('add',addView,name='add_url'),
    path('add/generate',genView,name='gen_url'),
    path('add/scan',scanView,name='scan_url'),
]
