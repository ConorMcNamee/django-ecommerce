from django.db import models

class Product(models.Model):
    product_id          = models.AutoField(primary_key=True)
    product_name        = models.CharField(max_length=30)
    product_desc        = models.CharField(max_length=300)
    product_price       = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.product_name