from django.urls import path
from .views import (
    PropertyListCreateView,
    PropertyDetailView,
    FavoriteListCreateView,
    FavoriteDeleteView,
)

urlpatterns = [
    path(
        "",
        PropertyListCreateView.as_view(),
        name="property-list-create",
    ),

    path(
        "<int:pk>/",
        PropertyDetailView.as_view(),
        name="property-detail",
    ),

    path(
        "favorites/",
        FavoriteListCreateView.as_view(),
        name="favorite-list-create",
    ),

    path(
        "favorites/<int:pk>/",
        FavoriteDeleteView.as_view(),
        name="favorite-delete",
    ),
]