from django.contrib import admin
from .models import Event


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('id', 'category', 'user', 'name', 'place', 'address',
                    'start_date', 'end_date', 'datetime', 'type', 'thumbnail')
