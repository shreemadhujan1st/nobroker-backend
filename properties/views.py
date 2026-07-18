from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Property
from .serializers import PropertySerializer
from .permissions import IsOwnerOrReadOnly


class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]