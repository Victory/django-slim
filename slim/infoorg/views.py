from django.shortcuts import render

from django.utils.translation import ugettext as _

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView)


class HomeView(TemplateView):
    template_name = "info-home.html"
