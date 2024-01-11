from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import exception_handler


def handle_exception(self, exc):
    if isinstance(exc, PermissionDenied):
        response_data = {
            "message": "Authentication is required to access this resource.",
            "status": status.HTTP_401_UNAUTHORIZED
        }
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return super().handle_exception(exc)