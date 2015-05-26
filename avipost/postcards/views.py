from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import FileUploadParser, JSONParser
from .models import Postcard
from .serializers import PostcardSerializer


class PostcardViewSet(viewsets.ModelViewSet):
    queryset = Postcard.objects.all()
    serializer_class = PostcardSerializer
    parser_classes = (FileUploadParser, JSONParser,)
    permission_classes = (permissions.IsAuthenticated,)

# Create your views here.
