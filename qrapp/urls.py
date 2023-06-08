from django.urls import path
from .views import homeView,searchView,successView

urlpatterns = [
    path('',homeView,name='home_url'),
    path('search/',searchView, name='review_url'),
    path('success/',successView,name='success_url')
]
