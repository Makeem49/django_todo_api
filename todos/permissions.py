from rest_framework import permissions


class IsStaffEdit(permissions.DjangoModelPermissions):
    
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # def has_permission(self, request, view):
    #     """This will check if the user staff user, else return false 
        
    #     which will make the user unable to have a permission to perform user 
        
    #     activities.

    #     """
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)

    # def has_permission(self, request, view):
    #     user = request.user 
    #     if not user.is_staff:
    #         return False

    #     if user.is_staff:
    #         """If user is a staff, and also have permissions to do 
    #         a lot of thing such has add, view, delete, update. 
    #         """
    #         if user.has_perm('todos.add_todo'):
    #             return True
    #         if user.has_perm('todos.view_todo'):
    #             return True
    #         if user.has_perm('todos.change_todo'):
    #             return True
    #         if user.has_perm('todos.delete_todo'):
    #             return True
    #     return False 