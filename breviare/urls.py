from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from breviare_urls.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'breviare.views.home', name='home'),
    # url(r'^breviare/', include('breviare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'shorten/$', 'breviare_urls.views.shorten_link'),
	url(r'visit/$', 'breviare_urls.views.link_click'),
	(r'^$', direct_to_template, {'template': 'index.html'}, "home"),
)
