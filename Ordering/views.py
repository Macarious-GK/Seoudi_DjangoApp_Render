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
            return Response(serializers_table1.data,status=status.HTTP_200_OK)
        except table1.DoesNotExist:
            return Response({"messega": "Item not found."}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializers_table1 = table1serralizer(data=request.data)
        serializers_table1.is_valid()
        serializers_table1.save()
        return Response(serializers_table1.data,201)
    else:
        return Response({'message':'this method is not supported'},405)
    
