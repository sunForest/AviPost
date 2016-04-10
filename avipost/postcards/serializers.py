from rest_framework import serializers
from .models import Postcard, Messenger
from django.contrib.auth.models import User


class MessengerSerializer(serializers.ModelSerializer):

    portrait = serializers.SerializerMethodField('get_portrait_url')

    def get_portrait_url(self, obj):
        return self.context['view'].request.build_absolute_uri(obj.portrait.url)

    class Meta:
        model = Messenger
        fields = ('id', 'name', 'portrait')


class PostcardReadSerializer(serializers.ModelSerializer):

    sender = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    cover = serializers.SerializerMethodField('get_cover_url')

    def get_cover_url(self, obj):
        return self.context['view'].request.build_absolute_uri(obj.cover.url)
    messenger = MessengerSerializer()

    class Meta:
        model = Postcard
        fields = ('id', 'message', 'cover', 'sender', 'latitude',
                  'longitude', 'messenger', 'image_height', 'image_width',
                  'cover_thumbnail_large', 'cover_thumbnail_medium',
                  'cover_thumbnail_small')


class PostcardWriteSerializer(serializers.HyperlinkedModelSerializer):

    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    messenger = serializers.PrimaryKeyRelatedField(
        queryset=Messenger.objects.all())

    class Meta:
        model = Postcard
        fields = ('message', 'cover', 'receiver', 'latitude',
                  'longitude', 'messenger')
