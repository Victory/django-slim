from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import home.views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home.views.DetailSlimView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
