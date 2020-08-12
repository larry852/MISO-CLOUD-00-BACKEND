from django.contrib import admin
from .models import Event


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('id', 'event_category', 'user', 'event_name', 'event_place', 'event_address',
                    'event_initial_date', 'event_final_date', 'datetime', 'event_type', 'thumbnail')
