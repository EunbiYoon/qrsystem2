from django.urls import path
from .views import homeView,searchView,checkoutView,addscanView,addView,addgenView,msgSuccessView,msgFailView

urlpatterns = [
    path('',homeView.as_view(),name='home_url'),
    path('search',searchView, name='search_url'),
    path('checkout',checkoutView,name="checkout_url"),
    path('add',addView,name='add_url'),
    path('add/generate',addgenView,name='addgen_url'),
    path('add/scan',addscanView,name='addscan_url'),
    path('success',msgSuccessView,name='msgsuccess_url'),
    path('failed',msgFailView,name='msgfail_url')
]
