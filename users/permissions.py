from rest_framework.permissions import BasePermission


class IsRecruiter(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == request.user.Role.RECRUITER:
            return True
        if request.user.is_superuser:
            return True
        return False


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == request.user.Role.ADMIN:
            return True
        if request.user.is_superuser:
            return True
        return False


class IsCandidate(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == request.user.Role.CANDIDATE:
            return True
        if request.user.is_superuser:
            return True

        return False

