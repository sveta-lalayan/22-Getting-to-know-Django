



from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from .forms import ProductForm
from .models import Product



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




def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})
