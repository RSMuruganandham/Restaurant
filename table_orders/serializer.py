from .models import DiningTable,Customer,Order
from menu_management.serializer import GetMenuItemSerializer
from rest_framework import serializers

class GetDiningTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningTable
        fields = ['table_number','seating_capacity','is_occupied']

class GetCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name','phone_number','email']
        
class GetOrderSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    table = serializers.SerializerMethodField()
    menu_items = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['customer','table','menu_items','order_time','is_completed','total_amount']
    def get_customer(self,obj):
        customer = obj.customer
        return GetCustomerSerializer(customer).data
        
    def get_table(self,obj):
        table = obj.table
        return GetDiningTableSerializer(table).data
    
    def get_menu_items(self,obj):
        menu_items = obj.menu_items
        return GetMenuItemSerializer(menu_items,many=True).data
    
    