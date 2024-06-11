from django import forms
from .models import LandListing

class LandListingForm(forms.ModelForm):
    class Meta:
        model = LandListing
        fields = ['title', 'description', 'price', 'image', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }