from rest_framework import serializers
from Ordering.models import *


class table1serralizer(serializers.ModelSerializer):
    class Meta:
        model = table1
        fields = '__all__'