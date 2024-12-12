from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")


def index(request):
    return render(request, "catalog/base.html")

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, "catalog/product_detail.html", {"product": product})


class HomePageView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "catalog/home.html", {"products": products})
