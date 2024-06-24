from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from authentication.serializers import LoginSerializer, UserSerializer


def get_csrf(request):
    response = JsonResponse({"detail": "CSRF cookie set"})
    response["X-CSRFToken"] = get_token(request)
    return response


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request: Request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(request, **serializer.validated_data)
    if not user:
        return Response({"detail": "Invalid credentials."}, status=400)
    login(request, user)
    return Response({"detail": "Successfully logged in."})


@api_view(["GET"])
@permission_classes([AllowAny])
def logout_view(request):
    if not request.user.is_authenticated:
        return Response({"detail": "You're not logged in."}, status=400)

    logout(request)
    return Response({"detail": "Successfully logged out."})


@api_view(["GET"])
def get_current_user(request: Request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data, 200)
