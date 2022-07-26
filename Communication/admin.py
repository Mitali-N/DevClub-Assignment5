from django.contrib import admin
from .models import Announcements, Message


class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ('announcement','course','instructor','datetime')


admin.site.register(Announcements, AnnouncementsAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender','to','message','date','time')


admin.site.register(Message, MessageAdmin)