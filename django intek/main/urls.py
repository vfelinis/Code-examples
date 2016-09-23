from django.conf.urls import patterns, include, url
from django.contrib.sitemaps.views import sitemap

from .sitemaps import ServiceSitemap, ArticleSitemap, StaticViewSitemap
from . import views

sitemaps = {
    'static' : StaticViewSitemap,
	'get_service' : ServiceSitemap,
    'get_article' : ArticleSitemap,
}

urlpatterns = patterns('',
    url(r'^$', 'main.views.home', name='home'),
    url(r'^yandex_6379745acdb3f8f4.html$', 'main.views.yandex', name='yandex'),
    url(r'^yandex_69b37a055164dea3.html$', 'main.views.yandex2', name='yandex2'),
    url(r'^google69bbe4774885e620.html$', 'main.views.google', name='google'),
    url(r'^message/$', 'main.views.message', name='message'),
    url(r'^about/$', 'main.views.about', name='about'),
    url(r'^contact/$', 'main.views.contact', name='contact'),
    url(r'^services/$', 'main.views.services', name='services'),
    url(r'^service/get/(?P<service_id>[0-9]+)/$', 'main.views.get_service', name='get_service'),
    url(r'^articles/$', 'main.views.articles', name='articles'),
    url(r'^article/get/(?P<article_id>[0-9]+)/$', 'main.views.get_article', name='get_article'),
    url(r'^test/$', 'main.views.test', name='test'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps' : sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
)