from django.conf.urls import patterns, url
from logs.views import SingleRequestView, RequestList

urlpatterns = patterns('',
    url(r'^$', RequestList.as_view(), name='logs_list'),
    url(r'^view/(?P<pk>\d+)/$', SingleRequestView.as_view(), name='logs_detail'),
)
