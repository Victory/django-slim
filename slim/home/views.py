from django.utils.translation import ugettext as _

from utilityslim.views import JSONResponseMixin

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView)


class DetailSlimView(TemplateView):
    template_name = 'home.html'


class SomeJsonView(JSONResponseMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = {}
        context['some_data'] = "some data"
        return context

    def render_to_response(self, context, **kwargs):
        return self.json_response(context, **kwargs)
