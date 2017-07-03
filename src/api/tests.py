from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Bucketlist


# Bucketlist Tests
class ModelTestCase(TestCase):
    def setUp(self):
        # Initialize a new bucketlist object passing a name
        self.bucketlist_name = 'Write world class code'
        self.bucketlist = Bucketlist(name=self.bucketlist_name)


    def test_can_create_a_bucketlist(self):
        # Check the current length of bucketlist objects
        old_count = Bucketlist.objects.count()
        # Try to add the new bucketlist
        self.bucketlist.save()
        # Check the length of bucketlist objects again
        new_count = Bucketlist.objects.count()
        # Compare between the old count and the new one
        # in order to check if the new bucketlist is in there
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(reverse('create'), self.bucketlist_data, format='json')


    def test_api_can_create_a_bucketlist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_api_can_get_a_bucketlist(self):
        # Send an id and try to get that bucketlist by id
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
            reverse('detials', kwargs={'pk': bucketlist.id}),
            format='json'
        )
        # Check response and bucketlist object
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)


    def test_api_can_update_a_bucketlist(self):
        change_bucketlist = {'name': 'Something new'}
        response = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)


    def test_api_can_delete_a_bucketlist(self):
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True
        )
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
