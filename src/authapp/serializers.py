from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    """Сериализатор регистрации."""

    password = serializers.CharField(
        write_only=True,
    )

    class Meta:
        model = User
        fields = ("username", "password")

    def create(self, validated_data):
        """Создает пользователя."""
        user = User.objects.create_user(**validated_data)
        return user
