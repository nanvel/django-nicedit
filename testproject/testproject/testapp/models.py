from django.db import models


class MessageModel(models.Model):
    content = models.TextField()
