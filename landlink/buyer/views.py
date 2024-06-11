from django.shortcuts import render, get_object_or_404

# Create your views here.
from seller.models import Location, LandListing


def dashboard(request):
    locations = Location.objects.all()
    listings = LandListing.objects.all()
    return render(request, 'buyer/dashboard.html', {'locations': locations, 'listings': listings})

def land_by_location(request, location_id):
    location = Location.objects.get(id=location_id)
    listings = LandListing.objects.filter(location=location)
    return render(request, 'buyer/land_by_location.html', {'location': location, 'listings': listings})


def view_listing_details(request, listing_id):
    listing = get_object_or_404(LandListing, pk=listing_id)

    # Render the view_details.html template with the listing object
    return render(request, 'buyer/view_details.html', {'listing': listing})