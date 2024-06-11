# buyer/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('location/<int:location_id>/', views.land_by_location, name='land_by_location'),
    path('listing/<int:listing_id>/', views.view_listing_details, name='view_listing_details'),
]