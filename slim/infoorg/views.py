from django.shortcuts import render

from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from infoorg.forms import InfoTipForm

from django.views.generic import (
    ListView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView)


class HomeView(FormView):
    template_name = "info-home.html"
    form_class = InfoTipForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_mail()
        return super(HomeView, self).form_valid(form)

    def get_success_url(self):
        return reverse('info-home')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['action'] = reverse('info-home')

        return context
