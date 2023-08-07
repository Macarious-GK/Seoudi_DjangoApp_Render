from django.db import models

# Create your models here.


class table1(models.Model):
    name = models.CharField(max_length=255)
    number = models.BigIntegerField()
    def __str__(self):
        return self.name
    


class Customer(models.Model):
    name = models.CharField(max_length=225)
    Phone = models.BigIntegerField()
    def __str__(self):
        return self.name