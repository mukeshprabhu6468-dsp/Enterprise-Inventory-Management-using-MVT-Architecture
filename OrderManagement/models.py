from django.db import models
from Inventory.models import Product

class Customer(models.Model):
    customer_name = models.CharField(max_length=200, null = True)
    customer_since = models.DateField(null = True)
    #customer_email = models.EmailField()
    #customer_phone = models.CharField(max_length=15)
    #customer_address = models.TextField()

    def __str__(self):
        return self.customer_name
    



class Order(models.Model):
    customer_reference = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product_reference = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(max_length=20,null=True,unique=True)
    order_date = models.DateField(null=True)
    quantity = models.IntegerField(null=True,default=0)
    amount = models.FloatField(null=True,default=0.0)
    gst = models.FloatField(null=True,default=0.0)
    bill_amount = models.FloatField(null=True,default=0.0)

    def __str__(self):
        return self.order_number

