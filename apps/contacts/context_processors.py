from django.conf import settings


def django_settings(request):
    '''
    Adds settins instance to context
    '''
    return {'settings': settings}
