from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import *
from .serializer import *

from rest_framework.decorators import api_view,permission_classes,throttle_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# CRUD Operations for Customers Table
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def customer_CR(request):
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer_customer = customerSerializer(customer,many = True)
        return Response({'Customers':serializer_customer.data},200)
    
    elif request.method == 'POST':
          serializer_customer = customerSerializer(data = request.data)
          serializer_customer.is_valid(raise_exception=True)
          serializer_customer.save()
          return Response(serializer_customer.data, 201)
    else:
         return Response({'message':'this method is not supported'},405)



@api_view(['GET','DELETE','PUT','PATCH'])
def customer_UD(request, pk):
    if request.method == 'GET':
        try:
            customer = Customer.objects.get(pk = pk)
            serializer_customer = customerSerializer(customer)
            return Response({'Customers':serializer_customer.data},200)
        except Customer.DoesNotExist:
             return Response({'message': 'Customer not found'}, status=404)
    
    elif request.method == 'DELETE':
        try:
            item = Customer.objects.get(pk=pk)
            item.delete()
            return Response({'Message':'customer deleted sussefully'},200)
        except Customer.DoesNotExist:
            return Response({"message": "Customer not found."}, status=404)
        
    elif request.method == 'PUT' or 'PATCH':  
        try:
            customer = Customer.objects.get(pk =pk)
            serializer_customer = customerSerializer(customer,data=request.data) 
            if serializer_customer.is_valid():
                serializer_customer.save()
                return Response(serializer_customer.data,status=200)
            return Response(serializer_customer.errors, status=400)
        except Customer.DoesNotExist:
            return Response({'message': 'Customer not found'}, status=404)
    else:
         return Response({'message':'this method is not supported'},status=405)
                
 
# CRUD Operatoins for Items Table

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@throttle_classes([AnonRateThrottle])
def item_CR(request):
    if request.method == 'GET':
        item = Order_Item.objects.all()
        serializer_item = ItemSerializer(item,many = True)
        return Response({'Customers':serializer_item.data},200)
    
    elif request.method == 'POST':
          serializer_item = ItemSerializer(data = request.data)
          serializer_item.is_valid(raise_exception=True)
          serializer_item.save()
          return Response(serializer_item.data, 201)
    else:
         return Response({'message':'this method is not supported'},405)



@api_view(['GET','DELETE','PUT','PATCH'])
@throttle_classes([AnonRateThrottle])
def item_UD(request, pk):
    if request.method == 'GET':
        try:
            item = Order_Item.objects.get(pk = pk)
            serializer_item = ItemSerializer(item)
            return Response({'items':serializer_item.data},200)
        except Order_Item.DoesNotExist:
             return Response({'message': 'item not found'}, status=404)
    
    elif request.method == 'DELETE':
        try:
            item = Order_Item.objects.get(pk=pk)
            item.delete()
            return Response({'Message':'item deleted sussefully'},200)
        except Order_Item.DoesNotExist:
            return Response({"message": "item not found."}, status=404)
        
    elif request.method == 'PUT' or 'PATCH':  
        try:
            item = Order_Item.objects.get(pk =pk)
            serializer_item = ItemSerializer(item,data=request.data) 
            if serializer_item.is_valid():
                serializer_item.save()
                return Response(serializer_item.data,status=200)
            return Response(serializer_item.errors, status=400)
        except Order_Item.DoesNotExist:
            return Response({'message': 'item not found'}, status=404)
    else:
         return Response({'message':'this method is not supported'},status=405)
                
# -----------------------------------------------------------

# CRUD operations on Order details table

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@throttle_classes([AnonRateThrottle])
def order_CR(request):
    if request.method == 'GET':
        order = Order_Details.objects.all()
        serializer_order = OrderSerializer(order,many = True)
        return Response({'Orders':serializer_order.data},200)
    
    elif request.method == 'POST':
          serializer_order = OrderSerializer(data = request.data)
          serializer_order.is_valid(raise_exception=True)
          serializer_order.save()
          return Response(serializer_order.data, 201)
    else:
         return Response({'message':'this method is not supported'},405)



@api_view(['GET','DELETE','PUT','PATCH'])
@throttle_classes([AnonRateThrottle])   
def order_UD(request, pk):
    if request.method == 'GET':
        try:
            order = Order_Details.objects.get(pk = pk)
            serializer_order = OrderSerializer(order)
            return Response({'Orders':serializer_order.data},200)
        except Order_Details.DoesNotExist:
             return Response({'message': 'Order not found'}, status=404)
    
    elif request.method == 'DELETE':
        try:
            order = Order_Details.objects.get(pk=pk)
            order.delete()
            return Response({'Message':'Order deleted sussefully'},200)
        except Order_Details.DoesNotExist:
            return Response({"message": "Order not found."}, status=404)
        
    elif request.method == 'PUT' or 'PATCH':  
        try:
            order = Order_Details.objects.get(pk =pk)
            serializer_order = OrderSerializer(order,data=request.data) 
            if serializer_order.is_valid():
                serializer_order.save()
                return Response(serializer_order.data,status=200)
            return Response(serializer_order.errors, status=400)
        except Order_Details.DoesNotExist:
            return Response({'message': 'Order not found'}, status=404)
    else:
         return Response({'message':'this method is not supported'},status=405)
                
#  ----------------------------------------------
# Get Status data
@api_view(['GET'])
@throttle_classes([AnonRateThrottle])
def status_R(request, pk):
    if request.method == 'GET':
        try:
            order = OrderStatus.objects.get(pk = pk)
            serializer_order = statusSerializer(order)
            return Response({'Status':serializer_order.data},200)
        except OrderStatus.DoesNotExist:
            return Response({'message': 'Status not found'}, status=404)
    
    else:
         return Response({'message':'this method is not supported'},405)
    

# Handeling Errors and Welcoming pages

def custom_404(request, exception):
    return render(request, '404.html', status=404)


def welcoming_page(request):
    return render(request, 'Welcome.html', status=200)
