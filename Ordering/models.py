from django.db import models

# Create your models here.


class Order_Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0.0)
    quantity = models.IntegerField(default=0.0)
    def __str__(self):
        return self.name 

class OrderStatus(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=225)
    Phone = models.BigIntegerField()
    def __str__(self):
        return self.name
    

class Order_Details(models.Model):
    orderNumber = models.AutoField(primary_key=True)
    orderDate = models.DateTimeField(auto_now = True, editable=False)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE,default = None)
    items = models.ManyToManyField(Order_Item)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE,default = None)
    flag = models.BooleanField(default=False)
    orderTotal = models.DecimalField(max_digits=10, decimal_places=2)
    orderTax = models.IntegerField()
    def __str__(self):
        return "Order "+str(self.orderNumber) +" : "+str(self.orderDate)
