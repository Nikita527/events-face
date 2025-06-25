from django.contrib import admin

from .models import Event, Venue


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    """Площадка для мероприятия."""

    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Мероприятие."""

    list_display = [
        "id",
        "name",
        "date",
        "status",
        "venue",
    ]
    search_fields = [
        "name",
    ]
    list_filter = [
        "status",
    ]
