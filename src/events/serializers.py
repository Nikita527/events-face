from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор мероприятия."""

    venue_name = serializers.CharField(
        source="venue.name", default=None, read_only=True
    )

    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "date",
            "status",
            "venue",
            "venue_name",
        ]
