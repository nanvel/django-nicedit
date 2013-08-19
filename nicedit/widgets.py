from django import forms
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe


class NicEditWidget(forms.Textarea):

    class Media:
        css = {
            'all': (
                staticfiles_storage.url('css/nicedit.css'),
            )
        }
        js = (
            staticfiles_storage.url('js/nicedit.js'),
        )
 
    def render(self, name, value, attrs=None):
        rendered = super(NicEditWidget, self).render(name, value, attrs=attrs)
        return rendered + mark_safe(u'''
<script>
    new nicEditor({uploadURI: '%s'}).panelInstance('id_%s');
</script>''' % (reverse('nicedit_upload'), name))
