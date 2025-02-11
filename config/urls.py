

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import contacts

app_name = CatalogConfig.name
#
urlpatterns = [

    path("", include("catalog.urls", namespace="catalog")),
    path(
        "contacts/", contacts, name="contacts"
    ),

    path("blog/", include('blog.urls', namespace='blog')),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



