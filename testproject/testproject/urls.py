from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'testproject.testapp.views.index', name='index'),
    url(r'^nicedit/', include('nicedit.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
