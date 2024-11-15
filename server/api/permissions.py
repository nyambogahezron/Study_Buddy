from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .models import User

# api permissions setup


class AuthenticateUser(BasePermission):
    def is_authenticated(self, request):
        try:
            token = request.COOKIES.get("access_token")
            if not token:
                print("No token")
                return False

            payload = UntypedToken(token)
            user_id = payload.get("user_id")
            use_info = User.objects.get(id=user_id)
            if not use_info:
                return False

            user = {
                "id": use_info.id,
                "email": use_info.email,
            }

            return user

        except (InvalidToken, TokenError, User.DoesNotExist):
            return False


class IsOwnerOrRoom(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ("GET", "HEAD", "OPTIONS", "POST" "PUT", "DELETE"):
            return True

        # Write permissions are only allowed to the owner of the object.
        user = AuthenticateUser().is_authenticated(request)
        if not user:
            return False

        return obj.host == user.get("id")


class CustomIsAuthenticated(BasePermission):
    """
    Custom permission to check if the user is authenticated.
    """

    def has_permission(self, request, view):
        try:
            token = request.COOKIES.get("access_token")
            if not token:
                return False

            payload = UntypedToken(token)
            user_id = payload.get("user_id")

            if not user_id:
                return False

            user = User.objects.get(id=user_id)
            request.user = user  # Attach the user to the request
            return True

        except (InvalidToken, TokenError, User.DoesNotExist):
            return False
