from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Property
from .permissions import IsOwnerOrReadOnly
from .serializers import PropertySerializer


class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = ["title", "location"]
    filterset_fields = ["price"]
    ordering_fields = ["price", "created_at"]
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