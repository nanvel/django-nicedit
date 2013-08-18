from django.db import models


class NicEditImageModel(models.Model):
    image = model.ImageField(upload_to='nicedit/%Y/%m/%d')
