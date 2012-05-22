from django.conf.urls import patterns, url
from contacts.views import PersonView

urlpatterns = patterns('',
    url(r'^$', PersonView.as_view(), name='contacts_home'),
)
