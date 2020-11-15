from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib import admin


class ShopUser(AbstractUser):
    funds = models.DecimalField(decimal_places=2, max_digits=12, default=10000.00)


class Products(models.Model):
    product_name = models.CharField(max_length=120, blank=False)
    description = models.TextField(blank=False, default='New description')
    number = models.PositiveIntegerField(blank=False)
    price_for_one = models.DecimalField(blank=False, decimal_places=2, max_digits=12,
                                        validators=[MinValueValidator(0.01)])


class Purchase(models.Model):
    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product')
    purchase_number = models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1)], )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class Return(models.Model):
    declined_product = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    request_time = models.DateTimeField(auto_now_add=True)
    request_status = models.CharField(max_length=120, default='Action required')


admin.site.register(ShopUser)
admin.site.register(Products)
admin.site.register(Purchase)
admin.site.register(Return)
