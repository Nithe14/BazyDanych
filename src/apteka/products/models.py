from django.db import models


class ProductManager(models.Manager):
    def add_product(self, name, price):
        if not name:
            raise ValueError("Product must have a name")
        if not price:
            raise ValueError("Product must have a price")

        product = self.create()

        product.name = name
        product.price = price

        product.save(using=self._db)
        return product

####################################################################################
class SimpleProduct(models.Model):
    name            = models.CharField(max_length=150, default='')
    producer        = models.CharField(max_length=150, default='')
    ex_date         = models.DateTimeField(auto_now_add=False)
    barcode         = models.BigIntegerField(primary_key=True, unique = True)
    dose            = models.CharField(max_length=50, default='')

    REQUIRED_FIELDS = ['name', 'producer', 'ex_date', 'barcode']

    ########GETS###########

    def get_name(self):
        return self.name
    def get_producer(self):
        return self.producer
    def get_ex_date(self):
        return self.ex_date
    def get_barcode(self):
        return self.barcode
    #######################

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

#####################################################################################
class Product(models.Model):
    name         = models.CharField(max_length=150, default='')
    producer     = models.CharField(max_length=150, default='')
    pharm_form = models.CharField(max_length=150, default='')
    price        = models.DecimalField(max_digits=20, decimal_places=2)
    description  = models.TextField()
    category     = models.TextField()
    ingredients  = models.TextField()
    stock        = models.IntegerField(default=0)

    REQUIRED_FIELDS = ['name', 'producer', 'price']
#######################GETS############################
    def get_name(self):
        return self.name
    def get_pharm_form(self):
        return self.name
    def get_price(self):
        return self.price
    def get_descritpion(self):
        return self.descritpion
    def get_category(self):
        return self.category
    def get_ingredients(self):
        return self.ingredients
    def get_ex_date(self):
        return self.ex_date
    def get_stock(self):
        return self.stock
    #############################
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    objects = ProductManager()

################################################################################


