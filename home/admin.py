from django.contrib import admin
from .models import School, Customer, Event

# Register your models here.
admin.site.register(School)
admin.site.register(Customer)
admin.site.register(Event)