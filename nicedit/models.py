from django.db import models


__all__ = ('NicEditImage',)


class NicEditImage(models.Model):
    image = models.ImageField(upload_to='nicedit/%Y/%m/%d')
