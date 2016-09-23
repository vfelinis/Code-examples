from django.conf.urls import include, url
from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticViewSitemap, UslugiSitemap, ProblemSitemap, OnasSitemap, SubmenuSitemap, SaleSitemap, ProductSitemap
from . import views

sitemaps = {
    'static' : StaticViewSitemap,
	'get_service' : UslugiSitemap,
    'get_problem' : ProblemSitemap,
    'get_onas' : OnasSitemap,
    'another' : SubmenuSitemap,
    'get_sale' : SaleSitemap,
    'get_product' : ProductSitemap,
}

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^yandex_6d5d0749557cc726.html$', views.yandex, name='yandex'),
    url(r'^another/(?P<url_name>.*)/$', views.another, name='another'),
    url(r'^product/(?P<product_id>[0-9]+)/$', views.get_product, name='get_product'),
    url(r'^googleb106583c234d7103.html$', views.google, name='google'),
    url(r'^message/$', views.message, name='message'),
    #url(r'^about/$', 'main.views.about', name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    #url(r'^services/$', 'main.views.services', name='services'),
    url(r'^service/get/(?P<service_id>[0-9]+)/$', views.get_service, name='get_service'),
    url(r'^sale/(?P<sale_id>[0-9]+)/$', views.get_sale, name='get_sale'),
    url(r'^o_nas/(?P<onas_id>[0-9]+)/$', views.get_onas, name='get_onas'),
    url(r'^problem/(?P<problem_id>[0-9]+)/$', views.get_problem, name='get_problem'),
    url(r'^sale/$', views.sale, name='sale'),
    #url(r'^articles/$', 'main.views.articles', name='articles'),
    #url(r'^article/get/(?P<article_id>[0-9]+)/$', 'main.views.get_article', name='get_article'),
    #url(r'^test/$', 'main.views.test', name='test'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps' : sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]