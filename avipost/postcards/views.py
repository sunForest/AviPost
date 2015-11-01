from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import FileUploadParser, JSONParser
from .models import Postcard
from .serializers import PostcardReadSerializer, PostcardWriteSerializer


class PostcardViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostcardReadSerializer
        return PostcardWriteSerializer

    def get_queryset(self):
        user = self.request.user
        return Postcard.objects.filter(receiver=user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    parser_classes = (FileUploadParser, JSONParser,)
    permission_classes = (permissions.IsAuthenticated,)
