from django.contrib import admin
from .models import DiningTable,Customer,Order
# Register your models here.

admin.site.register(DiningTable)
admin.site.register(Customer)
admin.site.register(Order)