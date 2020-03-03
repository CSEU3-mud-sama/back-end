from django.urls import include, path
from django.conf.urls import url
from .views import RoomviewAPI

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('adv/rooms/', RoomviewAPI.as_view()),
]
