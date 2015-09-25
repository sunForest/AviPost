from rest_framework import serializers
from .models import Postcard
from django.contrib.auth.models import User


class PostcardSerializer(serializers.HyperlinkedModelSerializer):

    sender = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    receiver = serializers.SlugRelatedField(write_only=True,
                                            slug_field='id',
                                            queryset=User.objects.all())

    class Meta:
        model = Postcard
        fields = ('message', 'cover', 'sender', 'receiver',)
