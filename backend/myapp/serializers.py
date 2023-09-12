# import serializers from the REST framework
from rest_framework import serializers

# import the video data model
from .models import Video, Game, Track, Cluster

# create a serializer class

class TrackSerializer(serializers.ModelSerializer):
	# create a meta class
	class Meta:
		model = Track
		fields = ('pred_cluster', 'true_cluster', 'bboxes', 'lifetime', 'video')

class ClusterSerializer(serializers.ModelSerializer):
	# videos = serializers.PrimaryKeyRelatedField(
	# 	many=True, required=False, read_only=True)
	pred_tracks = TrackSerializer(many=True, read_only=True)
	# create a meta class
	class Meta:
		model = Cluster
		fields = ('id', 'predicted', 'junk', 'person', 'pred_tracks',)

class VideoSerializer(serializers.ModelSerializer):
	clusters = ClusterSerializer(many=True, read_only=True)
	# tracks = TrackSerializer(many=True, read_only=True)
	# create a meta class
	class Meta:
		model = Video
		fields = ('name', 'game', 'clusters', 'fps', 'width', 'height')

class GameSerializer(serializers.ModelSerializer):
	# videos = serializers.PrimaryKeyRelatedField(
	# 	many=True, required=False, read_only=True)
	videos = VideoSerializer(many=True, read_only=True)
	# create a meta class
	class Meta:
		model = Game
		fields = ('id', 'date', 'title', 'videos',)
