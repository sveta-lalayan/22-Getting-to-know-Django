# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from .models import Article
#
#
# class ArticleListView(ListView):
#     model = Article
#
#
# class ArticleDetailView(DetailView):
#
#
#     def get(self, request, pk):
#         post = get_object_or_404(Article, pk=pk)
#         post.views_count += 1
#         post.save()
#         return super().get(request, pk)
#
#
# model = Article
#
# template_name = 'article_detail.html'
#
#
# class CreateArticle(CreateView):
#     template_name = 'create_article.html'
#
#
# model = Article
# fields = ['title', 'content', 'preview_image', 'is_published']
#
#
# class UpdateArticle(UpdateView):
#     template_name = 'update_article.html'
#
#
# model = Article
# fields = ['title', 'content', 'preview_image', 'is_published']
#
#
# class DeleteArticle(DeleteView):
#     success_url = '/articles/'
#
#
# template_name = 'delete_article.html'
# model = Article
# context_object_name = 'article'

from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title','content','image']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'

    def get_queryset(self):
        return Blog.objects.filter(publication=True)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object =super().get_object(queryset)
        self.object.number_views +=1
        self.object.save()
        return self.object

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')


