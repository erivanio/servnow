from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.core.views import ApiClientView

urlpatterns = patterns('',
    url(r'^API/users/$', ApiClientView.as_view(), name='api_users'),
)

admin.site.site_header = 'ServNow'