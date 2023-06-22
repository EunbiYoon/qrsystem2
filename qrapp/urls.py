from django.urls import path
from .views import homeView,searchView,scanView,genView,successView

urlpatterns = [
    path('',homeView.as_view(),name='home_url'),
    path('search/',searchView.as_view(), name='search_url'),
    path('scan/',scanView,name='scan_url'),
    path('add/',genView,name='add_url'),
    path('success/',successView,name='success_url')
]
