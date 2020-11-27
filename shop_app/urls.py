from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from shop_app.API import resources
from shop_app.views import ProductList, Login, Logout, Registration, PurchaseView, HistoryView, AddReturnView, \
    ReturnListView, ReturnActionView, CreateProductView, EditProductView

router = DefaultRouter()
router.register(r'users', resources.UserViewSet)
router.register(r'products', resources.ProductViewSet)
router.register(r'purchase', resources.PurchaseViewSet)
router.register(r'returns', resources.ReturnViewSet)

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', Registration.as_view(), name='registration'),
    path('purchases/', HistoryView.as_view(), name='purchase-history'),
    path('purchase/', PurchaseView.as_view(), name='purchase'),
    path('return/', AddReturnView.as_view(), name='return'),
    path('returns/', ReturnListView.as_view(), name='return-admin'),
    path('create/', CreateProductView.as_view(), name='create'),
    path('edit/<int:pk>/', EditProductView.as_view(), name='edit'),
    path('returns/action/', ReturnActionView.as_view(), name='approve-decline'),
    path('API/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
