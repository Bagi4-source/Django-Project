import jwt
from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        try:
            token = jwt.decode(request.headers.get('Authorization'), options={"verify_signature": False})
            return token.get("is_admin", False)
        except jwt.ExpiredSignatureError:
            return False
        
