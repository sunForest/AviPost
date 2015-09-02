from rest_framework import serializers
from .models import Postcard


class PostcardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Postcard
        fields = ('message', 'cover', 'sender',)
        read_only_fields = ('sender',)