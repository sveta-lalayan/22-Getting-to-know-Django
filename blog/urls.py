# from django.urls import path
# from .views import (
#      ArticleListView,
#      ArticleDetailView,
#      CreateArticle,
#      UpdateArticle,
#      DeleteArticle,
# )
#
# app_name = 'blog'
#
# urlpatterns=[
#      path('', ArticleListView.as_view(), name="article_list"),
#      path('<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
#      path('create/', CreateArticle.as_view(), name="create_article"),
#      path('<int:pk>/update/', UpdateArticle.as_view(), name="update_article"),
#      path('<int:pk>/delete/', DeleteArticle.as_view(), name="delete_article"),
#
# ]



from django.urls import path

from . import views
from .apps import BlogConfig
# from . import views
from .views import BlogListView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    # Список статей
    path('', views.BlogListView.as_view(), name='blog_list'),

    # Создание новой статьи
    path('create/', views.BlogCreateView.as_view(), name='blog_create'),

    # Детальный просмотр статьи
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),

    # Редактирование статьи
    path('<int:pk>/update/', views.BlogUpdateView.as_view(), name='blog_update'),

    # Удаление статьи
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete')
]

