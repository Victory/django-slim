from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import home.views
import infoorg.views

js_info_dict = {
    'packages': ('slim',),
}

urlpatterns = patterns(
    '',
    url(r'^$', home.views.DetailSlimView.as_view(), name='home'),
    url(r'^infoorg/$', infoorg.views.HomeView.as_view(), name='info-home'),
    url(r'^infoorg/infotip$',
        infoorg.views.InfoTipView.as_view(),
        name='info-tip'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
)
