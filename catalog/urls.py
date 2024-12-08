from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts
from catalog.views import ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [

    path("", HomePageView.as_view(), name="home"),
    # path("", home, name="home"),  # This is the root URL for the home page
    path(
        "contacts/", contacts, name="contacts"

    )
    path("product/<int:product_id>/", ProductDetailView.as_view(), name="product_detail"),

]



