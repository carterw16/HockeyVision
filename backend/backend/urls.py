"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from rest_framework import routers

# create a router object
router = routers.DefaultRouter()

# register the router
router.register(r'videos',views.VideoView, 'video')
router.register(r'games',views.GamesView, 'games')
router.register(r'tracks',views.TrackView, 'tracks')
router.register(r'clusters',views.ClusterView, 'clusters')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include(router.urls)),
    path('newview', views.NewView.as_view()),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
