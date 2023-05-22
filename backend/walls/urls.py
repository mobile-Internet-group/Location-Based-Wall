# walls/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from walls import views

router = DefaultRouter()
router.register('walls', views.WallsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]