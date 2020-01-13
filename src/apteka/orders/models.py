
from django.db import models
from accounts.models import User
from datetime import datetime

from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    recived = models.CharField(max_length=150, default="")
    payment = models.CharField(max_length=150, default="")
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    price = models.FloatField(blank=True)
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)