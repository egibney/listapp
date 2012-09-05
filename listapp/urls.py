from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from lists import urls

from django.conf.urls.static import static

from django.conf import settings

urlpatterns = patterns('',
	#url(r'^lists/$', 'lists.views.index'),
    # url(r'^$', 'listapp.views.home', name='home'),
    # url(r'^listapp/', include('listapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lists/', include(urls)),

)


if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.)$', static, {'document_root': settings.STATIC_ROOT}),
		#(r'^media/(?P<path>.)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
	)
 
