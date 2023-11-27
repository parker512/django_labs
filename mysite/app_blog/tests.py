from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class,
                          HomePageView)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomePageView)

    def test_articles_list_url(self):
        url = reverse('articles-list')
        self.assertEquals(resolve(url).func.view_class, ArticleList)

    def test_articles_category_list_url(self):
        url = reverse('articles-category-list', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, ArticleCategoryList)

    def test_news_detail_url(self):
        url = reverse('news-detail',
                      args=[2023, 11, 27, 'some-slug'])
        self.assertEquals(resolve(url).func.view_class, ArticleDetail)

class YourTestCase(TestCase):
    def test_something(self):
        self.assertTrue(True)