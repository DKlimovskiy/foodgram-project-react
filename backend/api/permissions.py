from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsNotBannedPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user and not request.user.is_active:
            return False

        return request.user.is_authenticated


class IsAuthorAdminOrReadOnlyPermission(IsNotBannedPermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return request.user == obj.author or request.user.is_staff
