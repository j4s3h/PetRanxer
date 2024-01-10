
from rest_framework.response import Response
from rest_framework import status, permissions

class CustomIsAuthenticated(permissions.IsAuthenticated):
    message = "Authentication is required to access this resource."
    code = status.HTTP_401_UNAUTHORIZED

    def permission_denied(self, request, message=None, code=None):
        response_data = {
            "message": "Oops, authentication failed.",  # Customize this message
            "status": self.code,
            "detail": self.message
        }
        return Response(response_data, status=self.code)