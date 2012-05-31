import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import SingleObjectMixin
from logs.models import Entry


#class ListRequests(ListView):
#    template_name = 'logs/index.html'
#    context_object_name = 'logs'
class SingleRequestView(SingleObjectMixin, TemplateView):
    model = Entry
    template_name = 'logs/detail.html'
    context_object_name = 'entry'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        rate = self.request.POST.get('rate')
        if rate == '1':
            self.object.priority += 1
            self.object.save()
        elif rate == '-1':
            self.object.priority -= 1
            self.object.save()
        else:
            return HttpResponseBadRequest(json.dumps('error'),
                    mimetype='application/json')
        return HttpResponse(json.dumps({'id': self.object.id,
            'priority': self.object.priority}), mimetype='application/json')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(SingleRequestView, self).dispatch(request, *args, **kwargs)


class RequestList(ListView):

    template_name = 'logs/index.html'
    context_object_name = 'logs'

    def get_queryset(self):
        sort = self.request.GET.get('descending')
        queryset = Entry.objects.all()
        if sort and sort == 'true':
            queryset = queryset.order_by('priority', 'dtime')
        else:
            queryset = queryset.order_by('-priority', 'dtime')
        return queryset[:10]

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            objects = [{'id': o.id,
                            'url': o.get_absolute_url(),
                            'dtime': o.dtime.strftime('%d.%m.%Y %H:%M:%S'),
                            'method': o.method,
                            'path': o.path,
                            'priority': o.priority} for o in self.get_queryset()]
            return HttpResponse(json.dumps(objects),
                    mimetype='application/json')
        else:
            return super(RequestList, self).get(request, *args, **kwargs)
