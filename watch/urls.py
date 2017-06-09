from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import (
    index_view,
    watch_list,
    detail_list,
    filter,
    contact_view
)

app_name = 'watch'

urlpatterns = [
    # /watch/
    url(r'^$', index_view, name='index'),
    url(r'^watch/$', watch_list, name='watch'),
    url(r'^watch/(?P<pk>[0-9]+)$', detail_list.as_view(), name='detail'),
    url(r'^search/$', filter),
    url(r'^contact/$', contact_view, name='contact'),
]
