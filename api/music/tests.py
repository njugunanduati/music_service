from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from api.music.models import Song
from api.music.serializers import SongsSerializer

# test for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Song.objects.create(title=title, artist=artist)

    def setUp(self):
        # add test data
        self.create_song("like glue", "Sean Paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")


class GetAllSongsTest(BaseViewTest):
    

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("songs-all", kwargs={"version":"v1"})
        )
        # fetch the data from the db
        expected = Song.objects.all()
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
