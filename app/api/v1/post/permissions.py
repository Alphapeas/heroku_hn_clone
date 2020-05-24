from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and obj.user == request.user or request.user.is_staff)
