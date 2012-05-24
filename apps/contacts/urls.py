from django.conf.urls import patterns, url
from contacts.views import PersonView, PersonUpdateView

urlpatterns = patterns('',
    url(r'^$', PersonView.as_view(), name='contacts_home'),
    url(r'^edit/', PersonUpdateView.as_view(), name='contacts_edit'),
)
