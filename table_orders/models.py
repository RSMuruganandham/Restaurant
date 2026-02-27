from django.db import models

from menu_management.models import BaseModel, MenuItem

# Create your models here.

class DiningTable(BaseModel):
    table_number = models.IntegerField()
    seating_capacity = models.IntegerField()
    is_occupied = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Table {self.table_number} "
class Customer(BaseModel):
    name = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=150,null=True,blank=True)
    def __str__(self):
        return f"{self.name}"
class Order(BaseModel):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    table= models.ForeignKey(DiningTable,on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(MenuItem)
    order_time = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=True)
    # total_amount = models.IntegerField() 
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"Order for {self.customer.name}"
    