from rest_framework import permissions

from .models import SellerProfile

class SellerUserPermission(permissions.BasePermission):

    def has_permission(self,request,view):
        if request.user.is_anonymous is not True:
            if SellerProfile.objects.filter(user=request.user).exists():
                return True
        return False