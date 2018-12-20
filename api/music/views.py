from rest_framework import generics
from api.music.models import Song
from api.music.serializers import SongsSerializer



class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler
    """
    queryset = Song.objects.all()
    serializer_class = SongsSerializer
