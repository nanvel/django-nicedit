from django.db import models


class NicEditImage(models.Model):
    image = models.ImageField(upload_to='nicedit/%Y/%m/%d')
