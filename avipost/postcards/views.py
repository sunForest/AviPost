from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import FileUploadParser, JSONParser
from .models import Postcard
# from django.contrib.auth.models import User
from .serializers import PostcardSerializer
import traceback


class PostcardViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        user = self.request.user
        return Postcard.objects.filter(receiver=user)

    def perform_create(self, serializer):
        try:
            serializer.save(sender=self.request.user)
        except Exception as e:
            print(e)
            traceback.print_exc()

    serializer_class = PostcardSerializer
    parser_classes = (FileUploadParser, JSONParser,)
    permission_classes = (permissions.IsAuthenticated,)
