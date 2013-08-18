from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('nicedit.views',
    url(r'^nicedit/upload/$', 'upload',vname='nicedit_upload'),
)
