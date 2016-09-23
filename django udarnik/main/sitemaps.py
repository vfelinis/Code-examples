from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from main.models import Sale, Service

class SaleSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Sale.objects.all()

    def location(self, obj):
        return '/sale/' + str(obj.id) + '/'

class ServiceSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Service.objects.all()

    def location(self, obj):
        return '/service/' + str(obj.id) + '/'

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items (self):
        return ['home', 'sales', 'message', 'about', 'contact']
 
    def location(self, item):
        return reverse(item)