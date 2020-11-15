from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from shop_app.models import ShopUser, Purchase, Products, Return


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class PurchaseForm(ModelForm):
    purchase_number = forms.IntegerField(label='', initial='1')

    class Meta:
        model = Purchase
        fields = ['purchase_number', ]


class CreateProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'description', 'number', 'price_for_one']


class AddReturnForm(ModelForm):
    class Meta:
        model = Return
        fields = []
