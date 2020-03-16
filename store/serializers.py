from rest_framework import serializers
from . import models

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=256)
    author = serializers.CharField(required=True, max_length=256)
    edithorial_id = serializers.IntegerField()
    
    def create(self, validated_data):
        instance = models.Book(**validated_data)
        instance.save()
        return instance

class EdithorialSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=250)
    
    
    def create(self, validated_data):
        instance = models.Edithorial(**validated_data)
        instance.save()
        return instance


