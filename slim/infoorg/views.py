from django.shortcuts import render

from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from django.views.generic import (
    ListView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView)

from infoorg.forms import InfoTipForm
from utilityslim.views import JSONResponseMixin


class HomeView(FormView):
    template_name = "info-home.html"
    form_class = InfoTipForm

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class InfoTipView(JSONResponseMixin, FormView):
    form_class = InfoTipForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_mail()
        return super(InfoTipView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = {}
        context['form_submited'] = True
        return context

    def render_to_response(self, context, **kwargs):
        return self.json_response(context, **kwargs)
