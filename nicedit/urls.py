from django.conf.urls import patterns, url


__all__ = ('urlpatterns',)


urlpatterns = patterns(
    'nicedit.views',
    url(r'^upload/$', 'upload', name='nicedit_upload'),
)
