from django.urls import path

from shop_app.views import ProductList, Login, Logout, Registration, PurchaseView, HistoryView, AddReturnView, \
    ReturnListView, ReturnActionView, CreateProductView, EditProductView

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
]
