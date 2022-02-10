from rest_framework.permissions import BasePermission


class AdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        return request.user.is_superuser == True