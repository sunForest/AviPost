from rest_framework import serializers
from .models import Postcard, Messenger
from django.contrib.auth.models import User


class MessengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messenger
        fields = ('name', 'portrait')


class PostcardReadSerializer(serializers.ModelSerializer):

    sender = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    messenger = MessengerSerializer()

    class Meta:
        model = Postcard
        fields = ('message', 'cover', 'sender', 'latitude',
                  'longitude', 'messenger')


class PostcardWriteSerializer(serializers.HyperlinkedModelSerializer):

    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    messenger = serializers.PrimaryKeyRelatedField(
        queryset=Messenger.objects.all())

    class Meta:
        model = Postcard
        fields = ('message', 'cover', 'receiver', 'latitude',
                  'longitude', 'messenger')
