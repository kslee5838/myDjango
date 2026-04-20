# Register your models here.
from django.contrib import admin
from .models import YourTrekking

@admin.register(YourTrekking)
class YourTrekkingAdmin(admin.ModelAdmin):
    list_display = ('trek_date', 'weekday', 'meeting_type', 'location', 'companion1')
    list_filter = ('weekday', 'meeting_type', 'location')
    search_fields = ('location', 'companion1', 'companion2', 'companion3', 'notes')
    date_hierarchy = 'trek_date'
    ordering = ('-trek_date',)


