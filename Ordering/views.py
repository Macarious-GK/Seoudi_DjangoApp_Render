from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import *
from .serializer import *

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser



@api_view(["GET",'POST'])
# @permission_classes([IsAuthenticated])
def order(request):
    if request.method == 'GET':
        try:
            table = table1.objects.all()
            serializers_table1 = table1serralizer(table,many = True)
            return Response(serializers_table1.data,200)
        except table1.DoesNotExist:
            return Response({"messega": "Item not found."}, 404)
    elif request.method == 'POST':
        serializers_table1 = table1serralizer(data=request.data)
        serializers_table1.is_valid()
        serializers_table1.save()
        return Response(serializers_table1.data,201)
    else:
        return Response({'message':'this method is not supported'},405)
    

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
                
 

