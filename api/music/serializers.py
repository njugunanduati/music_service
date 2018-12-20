from rest_framework import serializers
from api.music.models import Song


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("title", "artist")
