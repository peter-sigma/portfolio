# Create your views here.
# seller/views.py
from django.shortcuts import render, redirect
from .forms import LandListingForm
from .models import LandListing

def upload_land(request):
    if request.method == 'POST':
        form = LandListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard or any other page
    else:
        form = LandListingForm()
    return render(request, 'seller/upload_land.html', {'form': form})
