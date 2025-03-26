#
#
# from django.shortcuts import render, get_object_or_404, redirect
# from django.views import View
# from .models import Product
# from .forms import ProductForm
# from django.urls import reverse_lazy
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
#
# class ProductListView(ListView):
#     model = Product
#     template_name = 'product_list.html'
#     context_object_name = 'products'
#
# class ProductCreateView(LoginRequiredMixin, CreateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'create_product.html'
#     success_url = reverse_lazy('product_list')
#
#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#
# class OwnerAccessMixin(UserPassesTestMixin):
#     def test_func(self):
#         product = self.get_object()
#         return product.owner == self.request.user or self.request.user.is_staff
#
# class ProductUpdateView(LoginRequiredMixin,OwnerAccessMixin, UpdateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'update_product.html'
#     success_url = reverse_lazy('product_list')
#
# class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, OwnerAccessMixin, DeleteView):
#     model = Product
#     template_name = 'delete_product.html'
#     success_url = reverse_lazy('product_list')
#     permission_required = 'catalog.delete_product'
#
# class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
#     permission_required = 'catalog.can_unpublish_product'
#
#     def post(self, request, product_id):
#         product = get_object_or_404(Product, pk=product_id)
#         product.status = 'draft'
#         product.save()
#         return redirect('product_list')
#
# class ProductDetailView(View):
#     def get(self, request, product_id):
#         product = get_object_or_404(Product, id=product_id)
#         return render(request, "catalog/product_detail.html", {
#             "product": product,
#             "can_unpublish": request.user.has_perm('catalog.can_unpublish_product'),
#             "can_delete": request.user.has_perm('catalog.delete_product')
#         })
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
# class HomePageView(View):
#     def get(self, request):
#         products = Product.objects.all()
#         return render(request, "catalog/home.html", {"products": products})
#
# def contacts():
#     return None
#


from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .services import get_cached_products, get_products_by_category, invalidate_product_cache


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return get_cached_products()


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        invalidate_product_cache()
        return super().form_valid(form)


class OwnerAccessMixin(UserPassesTestMixin):
    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user or self.request.user.is_staff


class ProductUpdateView(LoginRequiredMixin, OwnerAccessMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        invalidate_product_cache(self.object.id)
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, OwnerAccessMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'catalog.delete_product'

    def delete(self, request, *args, **kwargs):
        product_id = self.get_object().id
        response = super().delete(request, *args, **kwargs)
        invalidate_product_cache(product_id)
        return response


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        product.status = 'draft'
        product.save()
        invalidate_product_cache(product_id)
        return redirect('product_list')


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(View):
    def get(self, request, product_id):
        cache_key = f'product_detail_{product_id}'
        product = cache.get(cache_key)

        if not product:
            product = get_object_or_404(Product, id=product_id)
            if product.status == 'published' or request.user.has_perm('catalog.view_draft_product'):
                cache.set(cache_key, product, 60 * 60)

        return render(request, "catalog/product_detail.html", {
            "product": product,
            "can_unpublish": request.user.has_perm('catalog.can_unpublish_product'),
            "can_delete": request.user.has_perm('catalog.delete_product')
        })


class CategoryProductsView(View):
    def get(self, request, category_slug):
        products = get_products_by_category(category_slug)
        category = products[0].category if products else None

        return render(request, "catalog/category_products.html", {
            "products": products,
            "category": category
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
        products = get_cached_products()[:8]
        return render(request, "catalog/home.html", {"products": products})

def contacts():
    return None
