import self as self
from rest_framework import permissions, request
from rest_framework.viewsets import ModelViewSet

from shop_app.API.serializers import UserSerializer, ProductSerializer, PurchaseSerializer, ReturnSerializer
from shop_app.models import ShopUser, Products, Purchase, Return


class UserViewSet(ModelViewSet):
    queryset = ShopUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,
                          ]
    http_method_names = ['get']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return ShopUser.objects.all()
        return ShopUser.objects.filter(id=user.id)


class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated,
                          ]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Purchase.objects.all()
        return Purchase.objects.filter(id=user.id)


class ReturnViewSet(ModelViewSet):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.IsAdminUser,
                          ]
