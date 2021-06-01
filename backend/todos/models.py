from django.db import models


class Product(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    price_currency = models.CharField(max_length=3)
    sku = models.CharField(max_length=20)
    total_sold = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
