from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
	url(r'^(\d+)$', views.detail, name="list_detail"),
	url(r'create_list', views.create_list, name="list_create_list"),
	url(r'', views.index),
)
