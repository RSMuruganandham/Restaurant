from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MenuCategory(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    is_active = models.BooleanField(default=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField()
    description = models.TextField(null=True,blank=True)
    is_available = models.BooleanField(default=True)
    categories = models.ManyToManyField(MenuCategory)
    
class Menu(models.Model):
    title = models.CharField(max_length=150)
    menu_items = models.ManyToManyField(MenuItem)
    is_active = models.BooleanField(default=True) 