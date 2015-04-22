from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser, JSONParser
from .models import Postcard
from .serializers import PostcardSerializer


class PostcardViewSet(viewsets.ModelViewSet):
    queryset = Postcard.objects.all()
    serializer_class = PostcardSerializer
    parser_classes = (FileUploadParser, JSONParser,)

# Create your views here.
