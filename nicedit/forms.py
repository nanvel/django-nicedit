from django import forms

from .models import NicEditImage


__all__ = ('NicEditImageForm',)


class NicEditImageForm(forms.ModelForm):

    class Meta:
        model = NicEditImage
        fields = '__all__'