from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('nicedit.views',
    url(r'^upload/$', 'upload', name='nicedit_upload'),
)
