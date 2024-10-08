from rest_framework import permissions

# SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAutherOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
    # def has_permission(self, request, view):
    #     return bool(
    #         request.method in SAFE_METHODS or
    #         request.user and
    #         request.user.is_authenticated
    #     )