from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.headers.get('x-userrole', None) == 'client'


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.headers.get('x-userrole', None) == 'admin'
