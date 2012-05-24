from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('contacts.urls')),
    url(r'^logs/', include('logs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
