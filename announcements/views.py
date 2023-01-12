from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from announcements.models import *
from announcements.serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AnnoucementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class AnnoucementOwnViewSet(APIView):
    queryset = Announcement.objects.none()

    def get(self,request,format=None):
        queryset = Announcement.objects.all()
        serializer = AnnouncementSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnnoucementOwnSetDetail(APIView):

    def get_object(self, pk):
        try:
            return Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        queryset = self.get_object(pk=pk)
        serializer = AnnouncementSerializer(queryset)
        return Response(serializer.data)