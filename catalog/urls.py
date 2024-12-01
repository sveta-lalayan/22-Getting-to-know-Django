from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),  # This is the root URL for the home page
    path(
        "contacts/", contacts, name="contacts"
    ),  # This is the URL for the contacts page
]
