from django.contrib import admin
from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('docname','document','course')


admin.site.register(Document, DocumentAdmin)