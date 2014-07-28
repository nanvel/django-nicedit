# -*- coding: utf-8 -*-
import json
from django import forms
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe


class NicEditWidget(forms.Textarea):

    def __init__(self, *args, **kwargs):
        self.js_options = kwargs.pop('js_options', {})
        super(NicEditWidget, self).__init__(*args, **kwargs)

    class Media:
        js = (
            staticfiles_storage.url('js/nicedit.min.js'),
        )

    def render(self, name, value, attrs=None):

        rendered = super(NicEditWidget, self).render(name, value, attrs=attrs)
        return rendered + mark_safe(u'''
<script>
    new nicEditor(%s).panelInstance('id_%s');
</script>''' % (self.js_options, name))


class NicEditAdminWidget(NicEditWidget):

    def render(self, name, value, attrs=None):
        if not isinstance(self.js_options, (unicode, str)):
            self.js_options['uploadURI'] = reverse('nicedit_upload')
            self.js_options = json.dumps(self.js_options)
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
        new nicEditor(%s).panelInstance(ta);
    }
</script>''' % (name, self.js_options))
