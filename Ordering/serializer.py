from rest_framework import serializers
from Ordering.models import *




class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Item
        fields = '__all__'

class statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['name']

class OrderSerializer(serializers.ModelSerializer):
    status = statusSerializer(read_only = True)

    class Meta:
        model = Order_Details
        fields = '__all__'