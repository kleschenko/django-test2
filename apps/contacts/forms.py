from django import forms
from django.utils.html import escape
from django.utils.safestring import mark_safe
from contacts.models import Person

attrs_right = {'class': 'right'}


class ImagePreviewInput(forms.FileInput):

    def __init__(self, *args, **kwargs):
        self.image_width = kwargs.pop('image_width', 330)
        super(ImagePreviewInput, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        result = super(forms.FileInput, self).render(name, value, attrs)
        if value and hasattr(value, "url"):
            preview = (u'<img src="%s" width="%s">' % (escape(value.url),
                self.image_width))
            result += '<br />' + preview

        return mark_safe(result)


class ContactsEditForm(forms.ModelForm):

    class Meta:
        model = Person
        widgets = {
                'email': forms.TextInput(attrs=attrs_right),
                'jabber': forms.TextInput(attrs=attrs_right),
                'skype': forms.TextInput(attrs=attrs_right),
                'other_contacts': forms.Textarea(attrs=attrs_right),
                'bio': forms.Textarea(attrs=attrs_right),
                'photo': ImagePreviewInput(image_width=330),
        }
        fields = ('name', 'surname', 'birth_date', 'photo', 'email',
                'jabber', 'skype', 'other_contacts', 'bio')
