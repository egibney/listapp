from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
	url(r'^(\d+)$', views.detail, name="list_detail"), 
	url(r'', views.index),
)
