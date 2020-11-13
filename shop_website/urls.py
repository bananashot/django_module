"""shop_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from shop_app.views import ProductList, Login, Logout, Registration, PurchaseView, HistoryView, AddReturnView, \
    ReturnListView, ReturnActionView, CreateProductView, EditProductView

urlpatterns = [
    path('admin/', admin.site.urls),
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
