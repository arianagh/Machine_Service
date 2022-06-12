from rest_framework.permissions import IsAuthenticated


class IsTechnician(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and\
               request.user.role == 'Technician'


class IsInspector(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and\
               request.user.role == 'Inspector'


class IsReception(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and\
               request.user.role == 'Reception'
