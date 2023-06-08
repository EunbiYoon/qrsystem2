from django.urls import path
from .views import homeView,searchView,scanView,genView

urlpatterns = [
    path('',homeView,name='home_url'),
    path('search/',searchView, name='search_url'),
    path('scan/',scanView,name='scan_url'),
    path('add/',genView,name='add_url')
]
