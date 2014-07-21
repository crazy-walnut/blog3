from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^register','blog.views.register'),
	url(r'^search-form','blog.views.search'),
	url(r'^biaoqian/$','blog.views.biaoqian'),
	url(r'^display/$','blog.views.display_meta'),
	url(r'^contact_form/$','blog.views.contact'),
	url(r'^index','blog.views.bootstrap'),
	url(r'^blog','blog.views.blog'),
	url(r'^login','blog.views.login'),
	url(r'^search','blog.views.search'),
	url(r'^time/plus/(\d{1,2})/$', 'blog.views.hours_ahead'),
)
