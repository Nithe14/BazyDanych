from django.db import models

class Opinion(models.Model):
    grade       = models.PositiveIntegerField()
    product_id  = models.ForeignKey('products.Product', on_delete=models.CASCADE, default="")
    #klien_id   = models.ForeignKey(#####)
