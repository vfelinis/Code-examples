from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from main.models import Service, Article

class ServiceSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Service.objects.all()

    def location(self, obj):
        return '/service/get/' + str(obj.id) + '/'

class ArticleSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Article.objects.all()

    def location(self, obj):
        return '/article/get/' + str(obj.id) + '/'

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items (self):
        return ['home', 'services', 'articles', 'message', 'about', 'contact']
 
    def location(self, item):
        return reverse(item)