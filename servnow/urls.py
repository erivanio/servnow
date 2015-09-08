from django.conf.urls import patterns, include, url
from django.contrib import admin
from servnow import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('apps.core.urls')),
)

urlpatterns += patterns('',
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^ckeditor/', include('ckeditor.urls')),
)

admin.site.site_header = 'ServNow'