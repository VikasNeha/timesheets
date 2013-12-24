from django.conf.urls import patterns, url

from myTimesheet import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)