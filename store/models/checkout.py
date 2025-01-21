from django.db import models
from .customer import Customer
from .product import Product
import datetime


class Checkout(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

