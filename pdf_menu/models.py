from django.db import models
from django.contrib.gis.geos import Point
from django.utils.text import slugify



class Address(models.Model):
    country = models.CharField(max_length=255, default='UAEB')
    emirate = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=22, decimal_places=16,
                              blank=True, null=True)
    long = models.DecimalField(max_digits=22, decimal_places=16,
                               blank=True, null=True)
    pin_code = models.IntegerField()

    @property
    def lat_long(self):
        return Point(self.lat, self.long)

class Menu(models.Model):
    pdf_data = models.FileField()
    menu_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shop(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    category = models.CharField(max_length=255, blank=False, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, default=None, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify([self.name, self.address.location])
        return super().save(*args, **kwargs)



    

