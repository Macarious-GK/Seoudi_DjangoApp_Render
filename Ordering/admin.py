from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Order_Item)
admin.site.register(Order_Details)
admin.site.register(Customer)
admin.site.register(OrderStatus)