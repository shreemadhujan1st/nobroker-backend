from rest_framework import serializers
from .models import Property, Favorite


class PropertySerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source="owner.username")
    owner_email = serializers.ReadOnlyField(source="owner.email")
    owner_phone = serializers.ReadOnlyField(source="owner.phone")

    class Meta:
        model = Property

        fields = [
            "id",
            "owner",
            "owner_email",
            "owner_phone",
            "title",
            "description",
            "listing_type",
            "price",
            "location",
            "property_type",
            "bedrooms",
            "bathrooms",
            "area",
            "image",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "owner",
            "owner_email",
            "owner_phone",
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