# buyer/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/buyer', views.buyer_registration, name='buyer_registration'),
    path('register/lawyer', views.seller_registration, name='seller_registration'),
    path('register/lawyer', views.lawyer_registration, name='lawyer_registration'),
    
]