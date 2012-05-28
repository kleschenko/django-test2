from django.views.generic import TemplateView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.http import Http404
from contacts.models import Person
from contacts.forms import ContactsEditForm


class PersonView(TemplateView):

    template_name = 'contacts/home.html'

    def get_context_data(self, **kwargs):
        context = super(PersonView, self).get_context_data(**kwargs)
        person = Person.objects.all()
        person = person[0] if person else None
        context['person'] = person
        return context


class PersonUpdateView(UpdateView):

    form_class = ContactsEditForm
    template_name = 'contacts/edit.html'
    success_url = '/'

    def get_object(self, queryset=None):
        try:
            obj = Person.objects.get(id=1)
        except ObjectDoesNotExist:
            raise Http404(u"No contacts records found in the database")
        return obj

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(PersonUpdateView, self).dispatch(request, *args, **kwargs)
