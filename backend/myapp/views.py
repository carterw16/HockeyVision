from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
from .forms import VideoForm

def showvideo(request):
    lastvideo = Video.objects.last()

    if lastvideo:
      videofile = lastvideo.videofile
    else:
        videofile = None

    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    
    context = {'videofile': videofile,
              'form': form
              }
    
    return render(request, 'myapp/video.html', context)

def index(request):
    return render(request, "myapp/index.html", context={})
