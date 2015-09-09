from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import FileUploadParser, JSONParser
from .models import Postcard
from .serializers import PostcardSerializer


class PostcardViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        user = self.request.user
        return Postcard.objects.filter(sender=user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    serializer_class = PostcardSerializer
    parser_classes = (FileUploadParser, JSONParser,)
    permission_classes = (permissions.IsAuthenticated,)
