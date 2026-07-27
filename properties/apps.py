from django.apps import AppConfig


class PropertiesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "properties"

    def ready(self):
        try:
            from django.contrib.auth import get_user_model
            from .models import Property

            if Property.objects.exists():
                return

            User = get_user_model()

            admin, _ = User.objects.get_or_create(
                username="admin",
                defaults={
                    "email": "admin@example.com",
                    "phone": "9999999999",
                    "is_staff": True,
                    "is_superuser": True,
                },
            )

            if not admin.has_usable_password():
                admin.set_password("admin123")
                admin.save()

            for i in range(1, 30):
                Property.objects.create(
                    owner=admin,
                    title=f"Sample Property {i}",
                    description="Beautiful property",
                    listing_type="Buy",
                    price=5000000 + i * 100000,
                    location="Bangalore",
                    property_type="Apartment",
                    bedrooms=2,
                    bathrooms=2,
                    area=1200,
                )

            print("Sample properties created.")

        except Exception:
            pass