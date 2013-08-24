from django.contrib import admin

from .models import Message
from .forms import MessageAdminForm


class MessageAdmin(admin.ModelAdmin):

    form = MessageAdminForm


admin.site.register(Message, MessageAdmin)
