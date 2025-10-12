from rest_framework import serializers
from .models import Expression

class ExpressionSerializer(serializers.ModelSerializer):
    # owner username read-only
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Expression
        fields = [
            "id", "text", "meaning", "region", "register",
            "usage_notes", "created", "owner",
        ]
        read_only_fields = ["created", "owner"]
