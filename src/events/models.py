import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from .schemas import StatusTextChoices


class Venue(models.Model):
    """Площадка."""

    id = models.UUIDField(
        verbose_name=_("ID"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(
        verbose_name=_("Название"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Площадка")
        verbose_name_plural = _("Площадки")
        ordering = ["name"]

    def __str__(self):
        """Возвращает название площадки."""
        return self.name


class Event(models.Model):
    """Мероприятие."""

    id = models.UUIDField(
        verbose_name=_("ID"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Название"),
    )
    date = models.DateTimeField(
        verbose_name=_("Дата"),
    )
    status = models.CharField(
        max_length=6,
        choices=StatusTextChoices.choices,
        default=StatusTextChoices.OPEN,
    )
    venue = models.ForeignKey(
        Venue,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="events",
    )

    class Meta:
        verbose_name = _("Мероприятие")
        verbose_name_plural = _("Мероприятия")
        ordering = ["-date"]

    def __str__(self):
        """Возвращает название мероприятия."""
        return self.name
