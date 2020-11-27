from django.contrib import admin

from shop_app.models import ShopUser, Products, Purchase, Return

admin.site.register(ShopUser)
admin.site.register(Products)
admin.site.register(Purchase)
admin.site.register(Return)
