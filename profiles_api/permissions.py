from rest_framework import permissions
from django.contrib.auth import get_user_model

# user= get_user_model()

class ProfileApiUpdatePermission(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self,request,view,obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class ProfileFeedUpdatePermission(permissions.BasePermission):
    
    
    def has_object_permission(self,request,view, obj):
        """Check wheather the user is authenticated for the update """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id