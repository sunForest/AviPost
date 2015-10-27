from random import random
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import FileUploadParser, JSONParser
from .models import Postcard
from .serializers import PostcardSerializer


class PostcardViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        user = self.request.user
        return Postcard.objects.filter(receiver=user)

    def perform_create(self, serializer):
        lat = random() * 160 - 80
        lon = random() * 360 - 180
        serializer.save(sender=self.request.user, longitude=lon, latitude=lat)

    serializer_class = PostcardSerializer
    parser_classes = (FileUploadParser, JSONParser,)
    permission_classes = (permissions.IsAuthenticated,)
