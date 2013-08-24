from django import forms
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe


class NicEditWidget(forms.Textarea):

    class Media:
        js = (
            staticfiles_storage.url('js/nicedit.min.js'),
        )
 
    def render(self, name, value, attrs=None):
        rendered = super(NicEditWidget, self).render(name, value, attrs=attrs)
        return rendered + mark_safe(u'''
<script>
    new nicEditor({uploadURI: '%s'}).panelInstance('id_%s');
</script>''' % (reverse('nicedit_upload'), name))


class NicEditAdminWidget(NicEditWidget):
 
    def render(self, name, value, attrs=None):
        rendered = super(NicEditWidget, self).render(name, value, attrs=attrs)
        return rendered + mark_safe(u'''
<script>
    var ta = document.getElementById('id_%s');
    if(ta) {
        var container = document.createElement('div');
        container.style.display = 'inline-block';
        container.style.float = 'left';
        ta.parentNode.insertBefore(container, ta);
        container.appendChild(ta);
        new nicEditor({uploadURI: '%s'}).panelInstance(ta);
    }
</script>''' % (name, reverse('nicedit_upload')))
