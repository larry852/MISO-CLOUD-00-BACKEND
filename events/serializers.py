from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data['event_initial_date'] > data['event_final_date']:
            raise serializers.ValidationError(
                {"event_initial_date": "Fecha de inicio está después de la fecha final."})
        return data

    class Meta:
        model = Event
        exclude = ('user', 'datetime', )
