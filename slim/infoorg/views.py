from django.shortcuts import render

from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext, loader

from django.views.generic import (
    ListView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView)

from infoorg.forms import InfoTipForm
from utilityslim.views import JSONFormMixin


class HomeView(FormView):
    template_name = "info-home.html"
    form_class = InfoTipForm

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class InfoTipView(JSONFormMixin, FormView):
    form_class = InfoTipForm
    success_url = '/infoorg/infotip'

    def render_form(self, form):
        t = loader.get_template('partials/info-tip-form.html')
        c = RequestContext(self.request, {"form": form})
        return t.render(c)

    def get_context_data(self, **kwargs):
        context = {}
        context['form_submited'] = True
        context['form_valid'] = True
        return context

    def render_to_response(self, context, **kwargs):
        return self.json_response(context, **kwargs)
