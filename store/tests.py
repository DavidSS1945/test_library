from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from store import models

class BookListTests(APITestCase):
    
    def test_create_book(self):
        url = reverse('book.list')
        data = {
            'name': 'test123',
            'author': 'test author',
            'edithorial': 'test edithorial '
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["author"], data["author"])
        self.assertEqual(response.data["edithorial"], data["edithorial"])
        self.assertIsNotNone(response.data.get("id"))


    def test_get_books(self):
        models.Book.objects.create(name="Bruce", author="Springsteen", edithorial="mangitos")
        models.Book.objects.create(name="Bruce2", author="Springsteen2",edithorial="mangitos2")

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
        models.Book.objects.create(name="Papachongo")
        models.Book.objects.create(name="Bronco")

        url = reverse('edithorial.list')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        