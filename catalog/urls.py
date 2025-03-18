

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ContactsView,
    IndexView,
    HomePageView,
    ProductDetailView,
)
from django.contrib import admin
from django.urls import path, include

from . import views
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [

    path("", HomePageView.as_view(), name="home"),


    path("contacts/", ContactsView.as_view(), name="contacts"),

    path(
        "product/<int:product_id>/",
        ProductDetailView.as_view(),
        name="product_detail"
    ),
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),

]











