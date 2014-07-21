from django.contrib import admin
from django import forms

from infoorg.models import Informer, InfoTip


class InformerForm(forms.ModelForm):
    class Meta:
        modle = Informer


class InformerAdmin(admin.ModelAdmin):
    form = InformerForm
    exclude = ['files', 'links', 'status', 'ip_notes']

admin.site.register(Informer, InformerAdmin)
admin.site.register(InfoTip)
