from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        # returns if the request method is safe (eg GET) or if user is admin
        return request.method in permissions.SAFE_METHODS or is_admin