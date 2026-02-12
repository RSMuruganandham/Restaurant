from rest_framework import serializers
from .models import MenuCategory, MenuItem, Menu

class GetMenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['name','description','is_active']
        
class GetMenuItemSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    class Meta:
        model = MenuItem
        fields = ['name','price','description','is_available','categories']
    def get_categories(self, obj):
        categories = obj.categories.all()
        for i in categories:
            return GetMenuCategorySerializer(i).data
        
class GetMenuSerializer(serializers.ModelSerializer):
    menu_items = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = ['title','menu_items','is_active']
    def get_menu_items(self,obj):
        menu_items = obj.menu_items.all()
        for i in menu_items:
            return GetMenuItemSerializer(i).data
        

    
    