from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from logs.models import Entry

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
            queryset=Entry.objects.order_by('-priority', 'dtime')[:10],
            template_name='logs/index.html',
            context_object_name='logs',
        ), name='logs_list'),
    url(r'^view/(?P<pk>\d+)/$', DetailView.as_view(
            model=Entry,
            template_name='logs/detail.html',
            context_object_name='entry',
        ), name='logs_detail'),
)
