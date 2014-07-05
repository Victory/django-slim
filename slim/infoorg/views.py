from django.shortcuts import render

from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from infoorg.forms import InfoTipForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView)


class HomeView(TemplateView):
    template_name = "info-home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['action'] = reverse('info-home')
        context['form'] = InfoTipForm()
        return context
