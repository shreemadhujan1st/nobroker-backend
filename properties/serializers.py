from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Property
        fields = [
            "id",
            "owner",
            "title",
            "description",
            "price",
            "location",
            "property_type",
            "bedrooms",
            "bathrooms",
            "area",
            "image",
            "created_at",
        ]