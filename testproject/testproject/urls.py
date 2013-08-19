from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'testproject.testapp.views.index', name='index'),
    url(r'^nicedit/', include('nicedit.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
