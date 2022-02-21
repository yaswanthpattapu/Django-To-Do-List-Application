from django.shortcuts import render
from .serializers import *
from .models import *

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class List(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        listobj = ListModel.objects.all()
        serializer = AppSerializer(listobj, many=True)
        return Response(serializer.data)


class Post_Single_List(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id, format=None):
        listobj = ListModel.objects.get(id=id)
        serializer = AppSerializer(listobj, many=False)
        try:
            return Response(serializer.data)
        except ListModel.DoesNotExist:
            raise Http404


class Post_List(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Update_List(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, id, format=None):
        listobj = ListModel.objects.get(id=id)
        serializer = AppSerializer(instance=listobj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Delete_List(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, id, format=None):
        listobj = ListModel.objects.get(id=id)
        listobj.delete()
        return Response("Item is deleted.")
