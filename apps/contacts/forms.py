from django import forms
from contacts.models import Person

attrs_right = {'class': 'right'}


class ContactsEditForm(forms.ModelForm):

    class Meta:
        model = Person
        widgets = {
                'email': forms.TextInput(attrs=attrs_right),
                'jabber': forms.TextInput(attrs=attrs_right),
                'skype': forms.TextInput(attrs=attrs_right),
                'other_contacts': forms.Textarea(attrs=attrs_right),
                'bio': forms.Textarea(attrs=attrs_right),
        }
        fields = ('name', 'surname', 'birth_date', 'photo', 'email',
                'jabber', 'skype', 'other_contacts', 'bio')
