from rest_framework import serializers
from .models import EmailStatus


class EmailStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailStatus
        fields = ["id", "email", "tracking_hash", "status", "created_at", "updated_at"]
