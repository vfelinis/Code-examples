from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from main.models import Uslugi, Submenu, Sale, Onas, Problem, Product

class UslugiSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Uslugi.objects.all()

    def location(self, obj):
        return '/service/get/' + str(obj.id) + '/'

class ProblemSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Problem.objects.all()

    def location(self, obj):
        return '/problem/' + str(obj.id) + '/'

class OnasSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Onas.objects.all()

    def location(self, obj):
        return '/o_nas/' + str(obj.id) + '/'

class SubmenuSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Submenu.objects.all()

    def location(self, obj):
        return '/another/' + str(obj.url) + '/'

class SaleSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Sale.objects.all()

    def location(self, obj):
        return '/sale/' + str(obj.id) + '/'

class ProductSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return '/product/' + str(obj.id) + '/'

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items (self):
        return ['home', 'sale', 'message', 'contact']
 
    def location(self, item):
        return reverse(item)