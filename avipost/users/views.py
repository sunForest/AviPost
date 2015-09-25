from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return User.objects.filter(is_staff=False)

    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
