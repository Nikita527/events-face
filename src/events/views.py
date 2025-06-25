from rest_framework import generics, filters, permissions

from .models import Event
from .serializers import EventSerializer


class EventListView(generics.ListAPIView):
    """Список мероприятий."""

    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["name"]
    ordering_fields = ["date"]
    ordering = ["date"]

    def get_queryset(self):
        """Возвращает список открытых мероприятий."""
        return Event.objects.filter(status="open").select_related("venue")
