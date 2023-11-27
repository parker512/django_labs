# app_blog /views.py
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Article, Category


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class ArticleList(ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'items'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleList, self).get_context_data(*args, **kwargs)
        try:
            context['category'] = Category.objects.get(slug=self.kwargs.get('slug'))
        except Exception:
            context['category'] = None
        return context

    def get_queryset(self, *args, **kwargs):
        articles = Article.objects.all()
        return articles
