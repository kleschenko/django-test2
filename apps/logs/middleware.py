from logs.models import Entry


class LogRequestsMiddleware(object):
    '''
    Middleware that stores all requests to db
    '''
    def process_request(self, request):
        keys = sorted(request.META.keys())
        meta = []
        for key in keys:
            if key.startswith('HTTP'):
                meta.append('%s: %s' % (key, request.META[key]))
        entry = Entry(method=request.method,
                path=request.path, meta='<br>'.join(meta))
        entry.save()
        return None
