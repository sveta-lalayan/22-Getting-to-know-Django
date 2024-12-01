

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts
from django.contrib import admin



app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),  # This is the root URL for the home page
    path(
        "contacts/", contacts, name="contacts"
    ),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)