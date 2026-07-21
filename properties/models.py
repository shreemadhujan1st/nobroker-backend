from django.db import models
from django.conf import settings


class Property(models.Model):
    PROPERTY_TYPES = [
        ("Apartment", "Apartment"),
        ("Villa", "Villa"),
        ("House", "House"),
        ("Plot", "Plot"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="properties",
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    location = models.CharField(max_length=255)

    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES,
        default="Apartment",
    )

    bedrooms = models.PositiveIntegerField(default=1)

    bathrooms = models.PositiveIntegerField(default=1)

    area = models.PositiveIntegerField(
        default=500,
        help_text="Area in Square Feet",
    )

    image = models.ImageField(
        upload_to="property_images/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title