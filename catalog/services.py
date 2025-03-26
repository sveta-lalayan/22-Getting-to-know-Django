from django.core.cache import cache
from .models import Product, Category


def get_cached_products():
    cache_key = 'all_products'
    products = cache.get(cache_key)

    if not products:
        products = Product.objects.filter(status='published').select_related('category')
        cache.set(cache_key, products, 60 * 60)  # 1 час
    return products


def get_products_by_category(category_slug):
    cache_key = f'products_category_{category_slug}'
    products = cache.get(cache_key)

    if not products:
        products = Product.objects.filter(
            category__slug=category_slug,
            status='published'
        ).select_related('category')
        cache.set(cache_key, products, 60 * 60)  # 1 час
    return products


def invalidate_product_cache(product_id=None):
    if product_id:
        cache.delete(f'product_detail_{product_id}')
    cache.delete('all_products')

    for cat in Category.objects.all():
        cache.delete(f'products_category_{cat.slug}')