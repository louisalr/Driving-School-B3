from django.contrib import admin
from .models import School, Customer, Booking

# Register your models here.
admin.site.register(School)
admin.site.register(Customer)
admin.site.register(Booking)
