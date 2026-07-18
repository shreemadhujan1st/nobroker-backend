from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Only the owner can edit or delete.
    Everyone authenticated can view.
    """

    def has_object_permission(self, request, view, obj):

        # Allow GET, HEAD, OPTIONS
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        # Allow only owner for PUT, PATCH, DELETE
        return obj.owner == request.user