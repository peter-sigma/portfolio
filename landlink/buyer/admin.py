from django.contrib import admin

# Register your models here.
from .models import Location, LandListing

admin.site.register(Location)
admin.site.register(LandListing)