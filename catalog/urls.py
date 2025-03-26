#
#
#
# from django.urls import path, include
# from django.contrib import admin
# from catalog.views import (
#     ContactsView,
#     IndexView,
#     HomePageView,
#     ProductDetailView,
#     ProductListView,
#     ProductCreateView,
#     ProductUpdateView,
#     ProductDeleteView,
#     ProductUnpublishView,
#
# )
#
# app_name = 'catalog'
#
# urlpatterns = [
#     path("", HomePageView.as_view(), name="home"),
#     path("contacts/", ContactsView.as_view(), name="contacts"),
#     path(
#         "product/<int:product_id>/",
#         ProductDetailView.as_view(),
#         name="product_detail"
#     ),
#     path('', ProductListView.as_view(), name='product_list'),
#     path('create/', ProductCreateView.as_view(), name='create_product'),
#     path('update/<pk>/', ProductUpdateView.as_view(), name='update_product'),
#     path('delete/<pk>/', ProductDeleteView.as_view(), name='delete_product'),
#     path('admin/', admin.site.urls),
#     path('products/<pk>/unpublish/', ProductUnpublishView.as_view(), name='unpublish_product'),
# ]


from django.urls import path, include
from django.contrib import admin
from catalog.views import (
    ContactsView,
    IndexView,
    HomePageView,
    ProductDetailView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductUnpublishView,
    CategoryProductsView
)

app_name = 'catalog'

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path(
        "product/<int:product_id>/",
        ProductDetailView.as_view(),
        name="product_detail"
    ),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('admin/', admin.site.urls),
    path('products/<pk>/unpublish/', ProductUnpublishView.as_view(), name='unpublish_product'),

    path('category/<slug:category_slug>/', CategoryProductsView.as_view(), name='category_products'),
]