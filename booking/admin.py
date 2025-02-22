from django.contrib import admin
from .models import Apartment,LandLord, Customer
admin.site.register(Apartment)

admin.site.register(LandLord)

admin.site.register(Customer)