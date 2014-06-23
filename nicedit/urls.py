from django.conf.urls import patterns, url


urlpatterns = patterns('nicedit.views',
    url(r'^upload/$', 'upload', name='nicedit_upload'),
)
