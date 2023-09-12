from django.shortcuts import render
from django.http import HttpResponse
from .models import Video, Game, Track, Cluster
from .forms import VideoForm
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from itertools import groupby


# import view sets from the REST framework
from rest_framework import viewsets
# import the TodoSerializer from the serializer file
from .serializers import VideoSerializer, GameSerializer, TrackSerializer, ClusterSerializer


class TrackView(viewsets.ModelViewSet):
	serializer_class = TrackSerializer
	queryset = Track.objects.all()

class VideoView(viewsets.ModelViewSet):
	serializer_class = VideoSerializer
	queryset = Video.objects.prefetch_related('clusters').all()

class GamesView(viewsets.ModelViewSet):
	serializer_class = GameSerializer
	queryset = Game.objects.prefetch_related('videos').all()

class ClusterView(viewsets.ModelViewSet):
	serializer_class = ClusterSerializer
	queryset = Cluster.objects.prefetch_related('pred_tracks').all()

class NewView(APIView):
	def get(self, request):
# 		game = Game.objects.prefetch_related('videos').get(id=22)
# 		ret = {}
# 		# print(game.videos.first())
# 		for video in game.videos.all():
# 			tracks = video.tracks.all()
# 			trackssort = sorted(tracks, key=key_func)
# 			trackquery = []

# 			for key, value in groupby(trackssort, key_func):
# 				trackquery.append()
# 			print(trackquery)
		return Response({'some': 'data'})