from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['title']


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListModel
        fields = ['id', 'Timestamp', 'Title', 'Description', 'DueDate', 'tags', 'Status']
        read_only_fields = ('id', 'Timestamp')
