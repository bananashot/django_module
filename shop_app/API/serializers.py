from rest_framework.serializers import ModelSerializer

from shop_app.models import Products, Purchase, ShopUser, Return


class UserSerializer(ModelSerializer):
    class Meta:
        model = ShopUser
        fields = ['username', 'first_name', 'last_name']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'product_name', 'description', 'number', 'price_for_one']


class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class ReturnSerializer(ModelSerializer):
    class Meta:
        model = Return
        fields = '__all__'
