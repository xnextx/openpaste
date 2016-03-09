from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase, APIRequestFactory
from .models import Inset
import json
import datetime


class AddInsetTests(APITestCase):
    def test_create_full_inset_no_private(self):
        """
        Test added new normal no-private Inset
        """

        response = self.client.post('/api/v1/Insets/',
                                    {
                                        'content': 'new idea', 'private': False, 'url_private': '',
                                        'date_added': datetime.datetime.today(), 'owner': None}, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Inset.objects.count(), 1)
        self.assertEqual(Inset.objects.get().content, 'new idea')
        self.assertEqual(Inset.objects.get().private, False)
        self.assertNotEqual(Inset.objects.get().url_private, '')
        self.assertNotEqual(Inset.objects.get().date_added, None)
        self.assertNotEqual(Inset.objects.get().url_private, '')
        self.assertNotEqual(Inset.objects.get().owner, '')
        self.assertEqual(Inset.objects.get().owner, None)

    def test_create_full_inset_private(self):
        """
        Test added new normal private Inset
        """

        response = self.client.post('/api/v1/Insets/',
                                    {'content': 'new idea', 'private': True, 'url_private': '',
                                     'date_added': datetime.datetime.today(), 'owner': None}, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Inset.objects.count(), 1)
        self.assertEqual(Inset.objects.get().content, 'new idea')
        self.assertEqual(Inset.objects.get().private, True)
        self.assertNotEqual(Inset.objects.get().url_private, '')
        self.assertNotEqual(Inset.objects.get().date_added, None)
        self.assertNotEqual(Inset.objects.get().url_private, '')
        self.assertNotEqual(Inset.objects.get().owner, '')
        self.assertEqual(Inset.objects.get().owner, None)

    def test_create_inset_empty_content_field(self):
        response = self.client.post('/api/v1/Insets/',
                                    {'content': '', 'private': True, 'url_private': '1',
                                     'date_added': datetime.datetime.today(), 'owner': None}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Inset.objects.count(), 0)

    def test_create_inset_empty_private_field(self):
        response = self.client.post('/api/v1/Insets/',
                                    {'content': '1', 'private': None, 'url_private': '',
                                     'date_added': datetime.datetime.today(), 'owner': None}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Inset.objects.count(), 0)

    def test_create_inset_empty_url_private_field(self):
        response = self.client.post('/api/v1/Insets/',
                                    {'content': '1', 'private': True, 'url_private': None,
                                     'date_added': datetime.datetime.today(), 'owner': None}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Inset.objects.count(), 0)

    def test_create_inset_empty_date_added_field(self):
        response = self.client.post('/api/v1/Insets/',
                                    {'content': '1', 'private': None, 'url_private': '',
                                     'date_added': None, 'owner': None}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Inset.objects.count(), 0)

    def test_create_inset_valid_date_added_field(self):
        response = self.client.post('/api/v1/Insets/',
                                    {'content': '1', 'private': None, 'url_private': '',
                                     'date_added': "QWERTY", 'owner': None}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Inset.objects.count(), 0)
