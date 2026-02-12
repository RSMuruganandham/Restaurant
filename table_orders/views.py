
from urllib import response
from django.shortcuts import render

from .models import DiningTable,Customer,Order
from rest_framework.views import APIView
from rest_framework.response import Response
from table_orders.serializer import GetDiningTableSerializer,GetCustomerSerializer,GetOrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication

# Create your views here.

class GetDiningTable(APIView):
    def get(self,request):
        table_number = request.query_params.get('table_number')
        is_available = request.query_params.get('is_occupied')
        dining_tables = DiningTable.objects.filter(table_number=table_number,is_occupied=is_available)
        serializer = GetDiningTableSerializer(dining_tables,many=True)
        return Response (serializer.data)
    
class GetCustomer(APIView):
    def get(self,request):
        name = request.query_params.get('name')
        phone_number = request.query_params.get('phone_number')
        email = request.query_params.get('email')
        customer = Customer.objects.filter(name=name,phone_number=phone_number,email=email)
        serializer = GetCustomerSerializer(customer,many=True)
        return Response(serializer.data)
    
class GetOrder(APIView):
    def get(self,request):
        customer = request.query_params.get('customer')
        table = request.query_params.get('table_number')
        order = Order.objects.filter(customer__name__icontains=customer,table__table_number=table) 
        serializer = GetOrderSerializer(order,many=True)
        return Response(serializer.data)    
    
    
# =================== Post Views =======================
class GetDiningTable(APIView):
    def post(self,request):
        table_number = request.data.get('table_number')
        is_available = request.data.get('is_occupied')
        dining_tables = DiningTable.objects.filter(table_number=table_number,is_occupied=is_available)
        serializer = GetDiningTableSerializer(dining_tables,many=True)
        return Response (serializer.data)
    
class GetCustomer(APIView):
    def post(self,request):
        name = request.data.get('name')
        phone_number = request.data.get('phone_number')
        email = request.data.get('email')
        # customer = Customer.objects.all()
        customer = Customer.objects.filter(name=name,phone_number=phone_number,email=email)
        serializer = GetCustomerSerializer(customer,many=True)
        return Response(serializer.data)
    
class GetOrder(APIView):
    def post(self,request):
        customer = request.data.get('customer')
        table_number = request.data.get('table_number')
        # order_time = request.data.get('order_time')
        is_complete = request.data.get('is_complete')
        total_amount = request.data.get('total_amount')
        order = Order.objects.filter(customer__name__icontains=customer,table__table_number=table_number,is_completed=is_complete,total_amount=total_amount)
        serializer = GetOrderSerializer(order,many=True)
        return Response(serializer.data)

# =================== Create Views =======================
class CreateCustomer(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    def post(self,request):
        data = request.data
        customer = {}
        customer['name'] = data['name']
        customer['phone_number'] = data['phone_number']
        customer['email'] = data['email']
        Customer.objects.create(**customer)
        return Response("Customer created successfully")
    
class CreateOrder(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    def post(self,request):
        data = request.data
        order = {}
        order['customer_id'] = data['customer_id']
        order['table_id'] = data['table_id']
        order['is_completed'] = data['is_completed']
        order['total_amount'] = data['total_amount']
        odr = data['menu_items']
        order_instance = Order.objects.create(**order)
        order_instance.menu_items.add(*odr)
        return Response("Order created successfully") 
    
class CreateDiningTable(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    def post(self,request):
        data = request.data
        dining_table = {}
        dining_table['table_number'] = data['table_number']
        dining_table['seating_capacity'] = data['seating_capacity']
        dining_table['is_occupied'] = data['is_occupied']
        DiningTable.objects.create(**dining_table)
        return Response("DiningTable Create Successfully")
     
# =================== Update Views =======================
class UpdateDiningTable(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    def post(self,request):
        data = request.data
        dining_table = DiningTable.objects.get(id=data['id'])
        dining_table.table_number = data['table_number']
        dining_table.seating_capacity = data['seating_capacity']
        dining_table.save()
        return Response('Dining Update Successfully')
    
class UpdateCustomer(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    def post(self,request):
        data = request.data 
        customer = Customer.objects.get(id=data['id'])
        customer.name = data['name']
        customer.phone_number = data['phone_number']
        customer.email = data['email']
        customer.save()
        return Response("Customer Update Successfully")
    
class UpdateOrder(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    def post(self,request):
        data = request.data 
        order = Order.objects.get(id=data['id'])
        order.customer = Customer.objects.get(id=data['customer'])
        order.table = DiningTable.objects.get(id=data['table'])
        order.menu_items.set(data['menu_items'])
        order.save()
        return Response("Order Update Successfully")
    
# =================== Delete Views =======================
class DeleteDiningTable(APIView):
    def post(self,request):
        data = request.data 
        dining_table = DiningTable.objects.get(id=data['id'])
        dining_table.delete()
        return Response("DiningTable Deleted Successfully")
    
class DeleteCustomer(APIView):
    def post(self,request):
        data = request.data 
        customer = Customer.objects.get(id=data['id'])
        customer.delete()
        return Response("Customer deleted Successfully")
    
class DeleteOrder(APIView):
    def post (self,request):
        data = request.data 
        order = Order.objects.get(id=data['id'])
        order.delete()
        return Response("Order Deleted Successfully")
    

# class RegisterCompany(APIView):
#     authentication_classes = [TokenAuthentication,SessionAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     def post(self,request):
#         data = request.data 
#         request_info = get_user_company_from_request(request)
#         user = get_user_from_request(request_info,data)
        
        
        
    
        

        