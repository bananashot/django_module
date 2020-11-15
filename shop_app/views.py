from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponseRedirect
from django.utils.datetime_safe import datetime
from django.views.generic import CreateView, ListView, UpdateView

from shop_app.forms import SignUpForm, PurchaseForm, AddReturnForm, CreateProductForm
from shop_app.models import ShopUser, Products, Purchase, Return
from django.contrib.auth import get_user_model

User = get_user_model()


class Registration(CreateView):
    model = ShopUser
    form_class = SignUpForm
    template_name = 'registration.html'
    success_url = '/'


class Login(LoginView):
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):

    def get(self, request, *args, **kwargs):
        logout(request.user)
        return super().get(request, *args, **kwargs)


class ProductList(ListView):
    model = Products
    template_name = 'products.html'
    paginate_by = 5
    queryset = Products.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({'form': PurchaseForm})
        return context


class PurchaseView(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = '/purchases/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.purchase_number = int(self.request.POST['purchase_number'])
        id_value = self.request.POST.get('id_value')
        product = Products.objects.get(id=id_value)

        request.session['product_id_error'] = int(id_value)

        if int(form.purchase_number) < 1:
            messages.error(request, 'You need to purchase at least 1 product')
            return HttpResponseRedirect('/')

        if product.number < form.purchase_number:
            messages.error(request, 'Not enough products, check the "Amount" field')
            return HttpResponseRedirect('/')

        if self.request.user.funds < product.price_for_one * form.purchase_number:
            messages.error(request, 'You need to add funds')
            return HttpResponseRedirect('/')

        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        purchase = form.save(commit=False)
        purchase.user = self.request.user
        purchase.purchase_number = int(self.request.POST['purchase_number'])

        current_user = ShopUser.objects.get(id=self.request.user.id)

        id_value = self.request.POST.get('id_value')

        product = Products.objects.get(id=id_value)

        current_user.funds -= purchase.purchase_number * product.price_for_one
        current_user.save()

        product.number -= purchase.purchase_number
        product.save()

        purchase.product = product
        purchase.save()

        return super().form_valid(form)


class HistoryView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'purchase.html'
    paginate_by = 5
    date_now = datetime.now()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({'now': self.date_now})
        return context

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user)


class AddReturnView(LoginRequiredMixin, CreateView):
    model = Return
    form_class = AddReturnForm
    success_url = '/purchases/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_value = self.request.POST.get('id_value')
        add_return = Purchase.objects.get(id=id_value)
        self.object.declined_product = add_return
        self.object.save()
        return super().form_valid(form)


class ReturnListView(LoginRequiredMixin, ListView):
    model = Return
    template_name = 'returns.html'
    paginate_by = 5

    def get_queryset(self):
        return Return.objects.filter(request_status='Action required')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({'form': AddReturnForm})
        return context


class ReturnActionView(LoginRequiredMixin, CreateView):
    model = Return
    form_class = AddReturnForm
    success_url = '/returns/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_value = self.request.POST.get('id_value')
        returned_product = Return.objects.get(id=id_value)
        product = Products.objects.get(id=returned_product.declined_product.product.id)
        current_user = User.objects.get(id=returned_product.declined_product.user.id)
        price_for_one = returned_product.declined_product.product.price_for_one
        purchased_number = returned_product.declined_product.purchase_number

        if 'action-approve' in self.request.POST:
            current_user.funds += price_for_one * purchased_number
            current_user.save()

            product.number += purchased_number
            product.save()

            returned_product.request_status = 'Approved'
            returned_product.save(update_fields=['request_status'])

        if 'action-decline' in self.request.POST:
            returned_product.request_status = 'Declined'
            returned_product.save(update_fields=['request_status'])

        return HttpResponseRedirect('/returns')


class CreateProductView(LoginRequiredMixin, CreateView):
    model = Products
    template_name = 'edit.html'
    form_class = CreateProductForm
    success_url = '/'


class EditProductView(LoginRequiredMixin, UpdateView):
    model = Products
    template_name = 'edit.html'
    success_url = '/'
    fields = ['product_name', 'description', 'number', 'price_for_one']
