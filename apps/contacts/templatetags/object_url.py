from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def edit_link(value):
    link = reverse('admin:%s_%s_change' %
            (value._meta.app_label, value._meta.module_name), args=[value.id])
    return '<a href="%s">%s</a>' % (link, value)
