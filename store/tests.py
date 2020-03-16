from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from store import models

class BookListTests(APITestCase):
    
    def test_create_book(self):
        url = reverse('book.list')
        edithorial = models.Edithorial.objects.create(name="Bruce")

        data = {
            'name': 'test123',
            'author': 'test author',
            'edithorial_id': edithorial.id
            
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["author"], data["author"])
        self.assertEqual(response.data["edithorial_id"], data["edithorial_id"])
        self.assertIsNotNone(response.data.get("id"))


    def test_get_books(self):
        edithorial = models.Edithorial.objects.create(name="Bruce")
        models.Book.objects.create(name="Bruce", author="Springsteen",  edithorial_id = edithorial.id)
        models.Book.objects.create(name="Bruce2", author="Springsteen2", edithorial_id = edithorial.id)

        url = reverse('book.list')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

class EdithorialListTests(APITestCase):
    
    def test_create_edithorial(self):
        url = reverse('edithorial.list')
        data = {
            'name': 'test',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], data["name"])
        self.assertIsNotNone(response.data.get("id"))


    def test_get_edithorial(self):
        models.Edithorial.objects.create(name="Papachongo")
        models.Edithorial.objects.create(name="Bronco")

        url = reverse('edithorial.list')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        