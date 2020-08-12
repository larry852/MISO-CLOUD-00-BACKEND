from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(source="name")
    event_category = serializers.CharField(source="category")
    event_place = serializers.CharField(source="place")
    event_address = serializers.DateTimeField(source="address")
    event_initial_date = serializers.DateTimeField(source="initial_date")
    event_final_date = serializers.CharField(source="final_date")
    event_type = serializers.CharField(source="type")

    class Meta:
        model = Event
        fields = ('id', 'event_name', 'event_category', 'event_place', 'event_address',
                  'event_initial_date', 'event_final_date', 'event_type', 'thumbnail')
