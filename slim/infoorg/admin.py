from django.contrib import admin

from infoorg.models import Informer, InfoTip


class InformerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Informer, InformerAdmin)
admin.site.register(InfoTip)
