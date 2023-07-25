import django.forms as forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "game", "url"]