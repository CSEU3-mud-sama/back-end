from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import include
from rest_framework.authtoken import views
from adventure.api import RoomViewSet

router = routers.DefaultRouter()
# register rooms with router to get into rooms api
router.register("rooms", RoomViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]