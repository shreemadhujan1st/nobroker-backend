from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters, status
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from .models import Property, Favorite
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    PropertySerializer,
    FavoriteSerializer,
)


class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "title",
        "location",
        "property_type",
    ]

    filterset_fields = [
        "price",
        "property_type",
        "bedrooms",
    ]

    ordering_fields = [
        "price",
        "created_at",
    ]

    ordering = ["-created_at"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]


class FavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        property_id = request.data.get("property")

        property_obj = get_object_or_404(
            Property,
            id=property_id,
        )

        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            property=property_obj,
        )

        serializer = FavoriteSerializer(favorite)

        if created:
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "message": "Property already in favorites."
            },
            status=status.HTTP_200_OK,
        )


class FavoriteDeleteView(generics.DestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(
            user=self.request.user
        )