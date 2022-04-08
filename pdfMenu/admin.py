from django.contrib import admin
from pdfMenu.models import Shop
from pdfMenu.models import Address


class ShopAdmin(admin.ModelAdmin):
    model = Shop
    exclude = ('')


# Register your models here.
admin.site.register(Shop)
admin.site.register(Address)
