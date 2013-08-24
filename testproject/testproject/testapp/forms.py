from django import forms

from nicedit.widgets import NicEditWidget, NicEditAdminWidget

from .models import Message


class MessageAdminForm(forms.ModelForm):

    class Meta:
        model = Message
        widgets = {
            'content': NicEditAdminWidget(attrs={'style': 'width: 800px;'}),
        }


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        widgets = {
            'content': NicEditWidget(attrs={'style': 'width: 800px;'}),
        }
