from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserRegisterSerializer
from rest_framework import generics


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer
