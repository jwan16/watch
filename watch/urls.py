from django.conf.urls import url
from django.contrib import admin
from .views import (
    index_view,
    watch_list,
    detail_list,
)

app_name = 'watch'

urlpatterns = [
    # /watch/
    url(r'^$', index_view, name='index'),
    url(r'^watch/$', watch_list, name='watch'),
    url(r'^watch/(?P<pk>[0-9]+)$', detail_list.as_view(), name='detail'),
    url(r'^watch/sort$', 'articles.views.sort_watch')
]
