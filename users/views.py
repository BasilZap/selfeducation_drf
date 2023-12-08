from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
