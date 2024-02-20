from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'movie', 'date', 'quantity', 'total_price', 'payment_method']
    list_filter = ['date', 'payment_method']
    search_fields = ['user__username', 'event__name', 'movie__title']
    date_hierarchy = 'date'
    ordering = ['date']

admin.site.register(Ticket, TicketAdmin)