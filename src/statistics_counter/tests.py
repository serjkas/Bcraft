from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import ActivityCollection
from .serializers import ActivityCollectionSerializer
from datetime import datetime


class ActivityTestCase(APITestCase):
    def setUp(self):

        self.type_1 = ActivityCollection.objects.create(
            views=1, clicks=1, cost=1)
        self.type_2 = ActivityCollection.objects.create(
            views=2, clicks=2, cost=2)

    def test_post(self):
        data_1 = {
            "views": 3,
            "clicks": 2,
            "cost": 1
        }
        response = self.client.post('/api/v1/activity/', data_1,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get(self):
        url = '/api/v1/activity/?from='+datetime.today().strftime(
            '%Y-%m-%d') + '&to=' + datetime.today().strftime('%Y-%m-%d')
        response = self.client.get(url)
        serializer_data = ActivityCollectionSerializer(
            [self.type_1, self.type_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_del(self):
        url = '/api/v1/delete_statistics'
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({"message": "Statistics was deleted"}, response.data)
