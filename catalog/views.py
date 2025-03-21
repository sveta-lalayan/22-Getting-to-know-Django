# from django.shortcuts import render, get_object_or_404, redirect
# from django.views import View
# from .models import Product
# from .forms import ProductForm
# from django.urls import reverse_lazy
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
#
#
# class ProductListView(ListView):
#     model = Product
#     template_name = 'product_list.html'
#     context_object_name = 'products'
#
#
# class ProductCreateView(LoginRequiredMixin, CreateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'create_product.html'
#     success_url = reverse_lazy('product_list')
#
# class ProductUpdateView(LoginRequiredMixin, UpdateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'update_product.html'
#     success_url = reverse_lazy('product_list')
#
# class ProductDeleteView(LoginRequiredMixin, DeleteView):
#     model = Product
#     template_name = 'delete_product.html'
#     success_url = reverse_lazy('product_list')
#
#
# class HomeView(View):
#     def get(self, request):
#         return render(request, "catalog/home.html")
#
# class ContactsView(View):
#     def get(self, request):
#         return render(request, "catalog/contacts.html")
#
# class IndexView(View):
#     def get(self, request):
#         return render(request, "catalog/base.html")
#
# class ProductDetailView(View):
#     def get(self, request, product_id):
#         product = get_object_or_404(Product, id=product_id)
#         return render(request, "catalog/product_detail.html", {"product": product})
#
# class HomePageView(View):
#     def get(self, request):
#         products = Product.objects.all()
#         return render(request, "catalog/home.html", {"products": products})
#
# def contacts():
#     return None


from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('product_list')


class HomeView(View):
    def get(self, request):
        return render(request, "catalog/home.html")

class ContactsView(View):
    def get(self, request):
        return render(request, "catalog/contacts.html")

class IndexView(View):
    def get(self, request):
        return render(request, "catalog/base.html")

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, "catalog/product_detail.html", {"product": product})

class HomePageView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "catalog/home.html", {"products": products})

def contacts():
    return None
