from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusTextChoices(models.TextChoices):
    """Выборы статуса."""

    OPEN = "open", _("Открыто")
    CLOSED = "closed", _("Закрыто")
