

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('product_list')




class OwnerAccessMixin(UserPassesTestMixin):
    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user or self.request.user.is_staff

class ProductUpdateView(LoginRequiredMixin,OwnerAccessMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, OwnerAccessMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'catalog.delete_product'

class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        product.status = 'draft'
        product.save()
        return redirect('product_list')

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, "catalog/product_detail.html", {
            "product": product,
            "can_unpublish": request.user.has_perm('catalog.can_unpublish_product'),
            "can_delete": request.user.has_perm('catalog.delete_product')
        })

class HomeView(View):
    def get(self, request):
        return render(request, "catalog/home.html")

class ContactsView(View):
    def get(self, request):
        return render(request, "catalog/contacts.html")

class IndexView(View):
    def get(self, request):
        return render(request, "catalog/base.html")

class HomePageView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "catalog/home.html", {"products": products})

def contacts():
    return None

