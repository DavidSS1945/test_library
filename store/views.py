from . import models
from . import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BookList(APIView):

    def get(self, request, format=None):
        books = models.Book.objects.all()
        serializer = serializers.BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    
    def get_object(self, pk):
        try:
            return models.Book.objects.get(pk=pk)
        except models.Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = serializers.BookSerializer(book)
        return Response(serializer.data)


class EdithorialList(APIView):
    
    def get(self, request, format=None):
        edithorial = models.Edithorial.objects.all()
        serializer = serializers.EdithorialSerializer(edithorial, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.EdithorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)