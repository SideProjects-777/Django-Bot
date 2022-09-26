from django.contrib import admin
from .models import TeleSetting


@admin.register(TeleSetting)
class TelegramAdmin(admin.ModelAdmin):
    list_display = ("tg_chat",'tg_message')
    search_fields  =("tg_chat",'tg_message')


