from django.db import models


__all__ = ('Message',)


class Message(models.Model):
    content = models.TextField()
