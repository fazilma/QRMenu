from django.contrib import admin
from pdf_menu.models import Shop
from pdf_menu.models import Address


class ShopAdmin(admin.ModelAdmin):
    model = Shop
    exclude = ('')


# Register your models here.
admin.site.register(Shop)
admin.site.register(Address)
