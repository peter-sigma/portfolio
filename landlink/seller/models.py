from django.db import models

# Create your models here.
from buyer.models import Location 
class LandListing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='land_images/')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, related_name='buyer_landlistings')

    def __str__(self):
        return self.title
