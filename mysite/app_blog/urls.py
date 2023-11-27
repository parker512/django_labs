from django.urls import path
from .views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail

urlpatterns = [
    path(r'', HomePageView.as_view()),
    path(r'articles', ArticleList.as_view(), name='articles-list'),
    path(r'articles/category/<slug>', ArticleCategoryList.as_view(), name='articles-category-list'),
    path(r'articles/<year>/<month>/<day>/<slug>', ArticleDetail.as_view(), name='news-detail'),
]
