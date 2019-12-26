from rest_framework.permissions import BasePermission
from api.exceptions import NotAuthenticated


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        raise NotAuthenticated()
