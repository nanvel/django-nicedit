from django import forms

from nicedit.widgets import NicEditWidget

from .models import Message


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        widgets = {
            'content': NicEditWidget,
        }
