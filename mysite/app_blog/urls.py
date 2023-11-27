from django.urls import path
from .views import HomePageView, ArticleList

urlpatterns = [
        path(r'', HomePageView.as_view()),
        path(r'articles', ArticleList.as_view(), name='articles-list')
]
