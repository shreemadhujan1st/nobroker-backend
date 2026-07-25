from django.urls import path

from .views import (
    PropertyListCreateView,
    PropertyDetailView,
    FavoriteListCreateView,
    FavoriteDeleteView,
    MyPropertiesView,
)

urlpatterns = [

    path(
        "",
        PropertyListCreateView.as_view(),
        name="property-list-create",
    ),

    path(
        "my-properties/",
        MyPropertiesView.as_view(),
        name="my-properties",
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

    path(
        "<int:pk>/",
        PropertyDetailView.as_view(),
        name="property-detail",
    ),

]