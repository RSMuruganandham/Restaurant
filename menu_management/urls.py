
from django.urls import path
from . import views

urlpatterns = [
    path('getMenuCategory',views.GetMenuCategory.as_view(),name='getMenuCategory'),
    path('getMenuItem',views.GetMenuItem.as_view(),name='getMenuItem'),
    path('getMenu',views.GetMenu.as_view(),name='getMenu'),
    path('createMenuCategory',views.CreateMenuCategory.as_view(),name='createMenuCategory'),
    path('createMenuItem',views.CreateMenuItem.as_view(),name='createMenuItem'),
    path('createMenu',views.CreateMenu.as_view(),name='createMenu'),
    path('updateMenuCategory',views.UpdateMenuCategory.as_view(),name='updateMenuCategory'),
    path('updateMenuItem',views.UpdateMenuItem.as_view(),name='updateMenuItem'),
    path('updateMenu',views.UpdateMenu.as_view(),name='updateMenu'),
    path('deleteMenuCategory',views.DeleteMenuCategory.as_view(),name='deleteMenuCategory'),
    path('deleteMenuItem',views.DeleteMenuItem.as_view(),name='deleteMenuItem'),
    path('deleteMenu',views.DeleteMenu.as_view(),name='deleteMenu'),
]
