from django.contrib import admin

# Register your models here.
from .models import LandListing, Location

admin.site.register(LandListing)
admin.site.register(Location)