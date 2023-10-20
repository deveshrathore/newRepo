from django.contrib import admin
from .models import Country,City,Hotel,PartnerShipBrands
#Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(PartnerShipBrands)
