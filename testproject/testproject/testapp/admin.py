from django.contrib import admin

from .models import Message
from .forms import MessageForm


class MessageAdmin(admin.ModelAdmin):

    form = MessageForm


admin.site.register(Message, MessageAdmin)
