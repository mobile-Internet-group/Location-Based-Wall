# wall/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from wall import views


router = DefaultRouter()
router.register('wall', views.WallsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]