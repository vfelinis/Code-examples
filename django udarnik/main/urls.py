from django.conf.urls import *
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, SaleSitemap, ServiceSitemap
from . import views

sitemaps = {
    'static' : StaticViewSitemap,
    'get_sale' : SaleSitemap,
    'get_service' : ServiceSitemap,
}

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^yandex_480de624f7674cc6.html$', views.yandex, name='yandex'),
    url(r'^google4ebc355ce8034adc.html$', views.google, name='google'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^message/$', views.message, name='message'),
    url(r'^sale/$', views.sales, name='sales'),
    url(r'^sale/(?P<sale_id>[0-9]+)/$', views.get_sale, name='get_sale'),
    url(r'^service/(?P<service_id>[0-9]+)/$', views.get_service, name='get_service'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps' : sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]