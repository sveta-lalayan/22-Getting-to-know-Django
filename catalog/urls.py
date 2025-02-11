

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ContactsView,
    IndexView,
    HomePageView,
    ProductDetailView,
)

app_name = CatalogConfig.name

urlpatterns = [

    path("", HomePageView.as_view(), name="home"),


    path("contacts/", ContactsView.as_view(), name="contacts"),

    path(
        "product/<int:product_id>/",
        ProductDetailView.as_view(),
        name="product_detail"
    ),

]

