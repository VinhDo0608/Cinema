from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'discount', 'time_start', 'time_end']
    list_filter = ['time_start', 'time_end']
    search_fields = ['title']
    date_hierarchy = 'time_start'
    ordering = ['time_start']

admin.site.register(Event, EventAdmin)