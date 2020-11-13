from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MinValueValidator
from django.forms import ModelForm
from django.http import HttpResponseRedirect

from shop_app.models import ShopUser, Purchase, Products, Return


class SignUpForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password1', 'password2')


class PurchaseForm(ModelForm):
    purchase_number = forms.IntegerField(label='', initial='1')

    class Meta:
        model = Purchase
        fields = ['purchase_number', ]


class CreateProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'number', 'price_for_one']


class AddReturnForm(ModelForm):
    class Meta:
        model = Return
        fields = []
