from django.conf.urls import url, include
from . import api
# from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from adventure.api import RoomViewSet


router = routers.DefaultRouter()
# register rooms with router to get into rooms api
router.register("rooms", RoomViewSet)

urlpatterns = [  
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]