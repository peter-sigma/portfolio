# seller/forms.py
from django import forms
from .models import LandListing

class LandListingForm(forms.ModelForm):
    class Meta:
        model = LandListing
        fields = ['title', 'description', 'price', 'image']
