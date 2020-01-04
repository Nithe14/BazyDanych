from django.db import models

class Producer (models.Model):
    name        = models.CharField(max_length=150, default="")
    nr_nip      = models.PositiveIntegerField()
    description  = models.TextField(45)

class Product(models.Model):
    name         = models.CharField(max_length=150, default="")
    producer_id  = models.ForeignKey('Producer', on_delete=models.CASCADE, default="")
    price        = models.DecimalField(max_digits=20, decimal_places=2)
    description  = models.TextField(45)
    category     = models.TextField(45)
    ingredients  = models.TextField(45)
    ex_date      = models.DateTimeField(auto_now=True, auto_now_add=False)
    stock        = models.IntegerField()
