from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import home.views


js_info_dict = {
    'packages': ('slim',),
}

urlpatterns = patterns('',
    url(r'^$', home.views.DetailSlimView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
)
