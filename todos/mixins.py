from rest_framework import permissions

from .permissions import IsStaffEdit

class PermissionStaffEditMixins(IsStaffEdit):
    permission_classes = [IsStaffEdit, permissions.IsAuthenticatedOrReadOnly]