from rest_framework import permissions


class TaskPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, task):
        return (
            request.user == task.author
            or request.user.is_staff
        )
