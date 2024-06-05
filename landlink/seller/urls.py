# seller/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_land, name='upload_land'),
]
