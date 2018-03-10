from django.contrib import admin
from .models import DocumentStatus, DocumentEntity

# Register your models here.


class DocumentStatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'description')
    search_fields = ('status',)


class DocumentEntityAdmin(admin.ModelAdmin):
    list_display = ('doc_id', 'status', 'owner', 'author', 'title')
    search_fields = ('doc_id', 'owner')


admin.site.register(DocumentStatus)
admin.site.register(DocumentEntity)