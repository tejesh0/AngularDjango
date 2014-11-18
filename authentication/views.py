
# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics
from authentication.serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer