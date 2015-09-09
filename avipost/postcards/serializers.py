from rest_framework import serializers
from .models import Postcard
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email',)


class PostcardSerializer(serializers.HyperlinkedModelSerializer):

    #sender = UserSerializer()
    sender = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Postcard
        fields = ('message', 'cover', 'sender',)