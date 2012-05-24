from django.views.generic import TemplateView
from contacts.models import Person


class PersonView(TemplateView):

    template_name = 'contacts/home.html'

    def get_context_data(self, **kwargs):
        context = super(PersonView, self).get_context_data(**kwargs)
        person = Person.objects.all()
        person = person[0] if person else None
        context['person'] = person
        return context
