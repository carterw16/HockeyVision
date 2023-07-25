from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
from .forms import VideoForm
from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets
# import the TodoSerializer from the serializer file
from .serializers import VideoSerializer

class VideoView(viewsets.ModelViewSet):
	serializer_class = VideoSerializer
	queryset = Video.objects.all()