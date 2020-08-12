from django.contrib import admin
from .models import Event


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('id', 'category', 'user', 'name', 'place', 'address',
                    'initial_date', 'final_date', 'datetime', 'type', 'thumbnail')
