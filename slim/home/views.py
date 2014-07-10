from django.utils.translation import ugettext as _

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView)


class DetailSlimView(TemplateView):
    template_name = 'home.html'
