from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.simple_tag
def edit_link(value):
    ct = ContentType.objects.get_for_model(value)
    link = reverse('admin:%s_%s_change' %
            (ct.app_label, ct.model), args=[value.id])
    return '<a href="%s">%s</a>' % (link, value)
