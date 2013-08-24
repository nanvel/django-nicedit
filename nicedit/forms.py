from django import forms

from .models import NicEditImage


class NicEditImageForm(forms.ModelForm):

    class Meta:
        model = NicEditImage
