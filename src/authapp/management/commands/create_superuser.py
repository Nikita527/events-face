import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Команда для создания суперпользователя.
    """

    def handle(self, *args, **options):
        if not User.objects.filter(
            username=os.getenv("SUPERUSER_USERNAME")
        ).exists():
            User.objects.create_superuser(
                username=os.getenv("SUPERUSER_USERNAME"),
                password=os.getenv("SUPERUSER_PASSWORD"),
            )
