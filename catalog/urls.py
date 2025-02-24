

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ContactsView,
    IndexView,
    HomePageView,
    ProductDetailView,
)

from . import views

app_name = CatalogConfig.name

urlpatterns = [

    path("", HomePageView.as_view(), name="home"),


    path("contacts/", ContactsView.as_view(), name="contacts"),

    path(
        "product/<int:product_id>/",
        ProductDetailView.as_view(),
        name="product_detail"
    ),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<pk>/update/', views.update_product, name='update_product'),
    path('products/<pk>/delete/', views.delete_product, name='delete_product'),

]



