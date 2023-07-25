# import serializers from the REST framework
from rest_framework import serializers

# import the video data model
from .models import Video

# create a serializer class
class VideoSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Video
		fields = ('name', 'game', 'url')
