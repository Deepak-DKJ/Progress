from django.contrib import admin
from .models import ChapterItem
# Register your models here.

@admin.register(ChapterItem)
class ChapterItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'pos','subject', 'chpName', 'status', 'note')

# admin.site.register(ChapterItem, ChapterItemAdmin)