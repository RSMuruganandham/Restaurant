from django.contrib import admin
from .models import MenuCategory,MenuItem,Menu

# Register your models here.

admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Menu)
