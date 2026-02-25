
from django.urls import path
from table_orders import views

urlpatterns = [
    path('getDiningTable',views.GetDiningTable.as_view(),name='getDiningTable'),
    path('getCustomer',views.GetCustomer.as_view(),name='getCustomer'),
    path('getOrder',views.GetOrder.as_view(),name='getOrder'),
    path('createCustomer',views.CreateCustomer.as_view(),name='createCustomer'),
    path('createOrder',views.CreateOrder.as_view(),name='createOrder'),
    path('createDiningTable',views.CreateDiningTable.as_view(),name='createDiningTable'),
    path('updateDiningTable',views.UpdateDiningTable.as_view(),name='updateDiningTable'),
    path('updateCustomer',views.UpdateCustomer.as_view(),name='updateCustomer'),
    path('updateOrder',views.UpdateOrder.as_view(),name='updateOrder')
] 

