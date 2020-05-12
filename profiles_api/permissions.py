from rest_framework import permissions
from django.contrib.auth import get_user_model

user= get_user_model()

class ProfileApiPermission(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self,request,view,obj):
        """Check user is trying to edit their own profile"""
        if request.method == permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

    