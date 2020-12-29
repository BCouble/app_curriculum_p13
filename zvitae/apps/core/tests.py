from django.test import TestCase, Client
from django.urls import reverse

class IndexPageTestCase(TestCase):

    def test_index_return(self):
        """ Test statut code IndexView """
        self.client = Client()
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
