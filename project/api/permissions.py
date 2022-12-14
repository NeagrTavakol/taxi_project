from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsOwnerOrAuthentication(BasePermission):

    def has_object_permission(self, request, view, obj):
        # if request.method in SAFE_METHODS:
        #     return True

        return bool(
             (request.user.is_authenticated and request.user.is_superuser) or
             (request.user.is_authenticated and obj == request.user) 
        ) 

class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)    


class IsSuperUserOrAuthentication(BasePermission):

    def has_permission(self, request, view):
        return bool(
             (request.user.is_authenticated and request.user.is_superuser) or
             (request.user.is_authenticated ) 
        ) 


