from django.db import models

class Order(models.Model):
    date    = models.DateTimeField(auto_now=True, auto_now_add=False)
    recived = models.CharField(max_length=150, default="")
    payment = models.CharField(max_length=150, default="")
    status  = models.CharField(max_length=45, default="")

class OrdersProducts(models.Model):
    order_id   = models.ForeignKey('Order', on_delete=models.CASCADE, default="")
    product_id = models.ForeignKey('products.Product', on_delete=models.CASCADE, default="")
    amount     = models.IntegerField()
