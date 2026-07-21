from rest_framework import serializers

from .models import Property, Favorite


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


class FavoriteSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(
        queryset=Property.objects.all(),
        source="property",
        write_only=True,
    )

    class Meta:
        model = Favorite
        fields = [
            "id",
            "property",
            "property_id",
        ]