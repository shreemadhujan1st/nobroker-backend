from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.files import File
from properties.models import Property

import random
import os

User = get_user_model()


class Command(BaseCommand):
    help = "Seed 30 sample properties with images"

    def handle(self, *args, **kwargs):

        owner = User.objects.first()

        if not owner:
            self.stdout.write(
                self.style.ERROR("Create a user first.")
            )
            return

        Property.objects.all().delete()

        cities = [
            "Bangalore",
            "Mysore",
            "Hyderabad",
            "Chennai",
            "Mumbai",
            "Pune",
            "Delhi",
            "Noida",
            "Kolkata",
            "Ahmedabad",
        ]

        property_types = [
            "Apartment",
            "Villa",
            "House",
            "Plot",
        ]

        image_folder = "media/property_images"

        image_files = [
            f for f in os.listdir(image_folder)
            if f.lower().endswith(
                (".jpg", ".jpeg", ".png", ".webp")
            )
        ]

        if not image_files:
            self.stdout.write(
                self.style.ERROR("No images found in media/property_images")
            )
            return

        for i in range(1, 31):

            city = random.choice(cities)
            ptype = random.choice(property_types)

            property_obj = Property.objects.create(
                owner=owner,
                title=f"{random.randint(1,4)} BHK {ptype} #{i}",
                description=f"Beautiful {ptype.lower()} located in {city}. Spacious rooms, modern amenities, and excellent connectivity.",
                price=random.randint(2500000, 25000000),
                location=city,
                property_type=ptype,
                bedrooms=random.randint(1,5),
                bathrooms=random.randint(1,4),
                area=random.randint(600,3500),
            )

            image_name = random.choice(image_files)

            image_path = os.path.join(
                image_folder,
                image_name,
            )

            with open(image_path, "rb") as img:
                property_obj.image.save(
                    image_name,
                    File(img),
                    save=True,
                )

        self.stdout.write(
            self.style.SUCCESS(
                "✅ 30 properties with images created successfully!"
            )
        )