from urllib import response
from django.shortcuts import render

from .models import MenuCategory, MenuItem, Menu
from rest_framework.views import APIView
from rest_framework.response import Response
from menu_management.serializer import GetMenuCategorySerializer,GetMenuItemSerializer,GetMenuSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication

# Create your views here.

class GetMenuCategory(APIView):
    def get(self,request):
        name = request.query_params.get('name')
        description = request.query_params.get('description')
        is_active = request.query_params.get('is_active')
        categories = MenuCategory.objects.filter(name=name,description=description,is_active=is_active)
        serializer = GetMenuCategorySerializer(categories,many=True)
        return Response(serializer.data) 
    
class GetMenuItem(APIView):
    def get(self,request):
        menu_items = MenuItem.objects.all()
        serializer = GetMenuItemSerializer(menu_items,many=True)
        return Response(serializer.data)
    
class GetMenu(APIView):
    def get(self,request):
        menu = Menu.objects.all()
        serializer = GetMenuSerializer(menu,many=True)
        return Response(serializer.data)
      

class GetMenuCategory(APIView):
    def post(self,request):
        name = request.data.get('name')
        description = request.data.get('description')
        is_active = request.data.get('is_active')
        categories = MenuCategory.objects.filter(name=name,description=description,is_active=is_active)
        serializer = GetMenuCategorySerializer(categories,many=True)
        return Response(serializer.data)
    
class GetMenuItem(APIView):
    def post(self,request):
        name = request.data.get('name')
        price = request.data.get('price')
        description = request.data.get('description')
        is_available = request.data.get('is_available')
        categories = request.data.get('categories')
        # menu_items = MenuItem.objects.all()
        menu_items = MenuItem.objects.filter(name=name,price=price,description=description,is_available=is_available,categories__name=categories)
        serializer = GetMenuItemSerializer(menu_items,many=True)
        return Response(serializer.data)
    
class GetMenu(APIView):
    def post(self,request):
        title = request.data.get('title')
        menu_item = request.data.get('menu_item')
        is_active = request.data.get('is_active')
        menu = Menu.objects.filter(title=title,menu_item=menu_item,is_active=is_active)
        serializer = GetMenuSerializer(menu,many=True)
        return Response(serializer.data)
    
# ================== Create Views =======================
class CreateMenuCategory(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    def post(self,request):
        data = request.data
        category = {}
        category ['name'] = data['name']
        category['description'] = data['description']
        category['is_active'] = data['is_active'] 
        MenuCategory.objects.create(**category)
        return Response("MenuCategory created successfully") 
    
class CreateMenuItem(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    def post(self,request):
        data = request.data
        menu_item = {}
        menu_item ['name'] = data['name']
        menu_item['price'] = data['price']
        menu_item['description'] = data['description']
        menu_item['is_available'] = data['is_available']
        # menu_item['categories'] = data['categories']
        item = data['categories']
        menu_item_instance = MenuItem.objects.create(**menu_item)
        menu_item_instance.categories.add(*item)
        return Response("MenuItem created successfully")
    
class CreateMenu(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    def post(self,request):
        data = request.data
        menu = {}
        menu ['title'] = data['title']
        menu ['is_active'] = data['is_active']
        menu_items = data['menu_items']
        menu_instance = Menu.objects.create(**menu)
        menu_instance.menu_items.add(*menu_items)
        return Response("Menu Created Successfully")

# ================== Update Views =======================
class UpdateMenuCategory(APIView):
    def post(self,request):
        data = request.data
        menuCategory = MenuCategory.objects.get(id=data['id'])
        menuCategory.name = data['name']
        menuCategory.save()
        return Response("MenuCategory updated successfully")
        
class UpdateMenuItem(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes =[TokenAuthentication,SessionAuthentication]
    def post(self,request):
        data = request.data
        menuItem = MenuItem.objects.get(id=data['id'])
        menuItem.name = data['name']
        menuItem.price = data['price']
        menuItem.description = data['description']
        menuItem.is_available = data['is_available']
        menuItem.save()
        return Response('MenuItem updated successfully')
        
class UpdateMenu(APIView):
    def post(self,request):
        data = request.data
        menu = Menu.objects.get(id=data['id'])
        menu.title = data['title']
        menu.save()
        return Response('Menu updated successfully')
    
# ================= Delete Views =======================
class DeleteMenuCategory(APIView):
    def post(self,request):
        data = request.data
        menuCategory = MenuCategory.objects.get(id=data['id'])
        menuCategory.delete()
        return Response("MenuCategory Deleted Successfully")
    
class DeleteMenuItem(APIView):
    def post(self,request):
        data = request.data 
        menuItem = MenuItem.objects.get(id=data['id'])
        menuItem.delete()
        return Response("MenuItem Deleted Successfully")
    
class DeleteMenu(APIView):
    def post(self,request):
        data = request.data 
        menu =Menu.objects.get(id=data['id'])
        menu.delete()
        return Response("Menu Deleted Successfully")
        