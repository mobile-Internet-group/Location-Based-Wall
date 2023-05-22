# walls/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from walls import views

router = DefaultRouter()
router.register('user/register', views.UserRegisterView)
router.register('user/login', views.UserLoginView)
router.register('post/{post_id}', views.PostsViewSet)
router.register('post/{post_id}', views.PostsViewSet)
router.register('comment/', views.CommentsViewSet)

urlpatterns = router.urls
'''[
    path('', include(router.urls)),
    path('user/register', include(router.urls)),#get
    path('user/login', include(router.urls)),#post
    path('post/{post_id}', include(router.urls)),#put
    path('post/{post_id}', include(router.urls)),#get
    path('comment', include(router.urls)),#get
    path('comment', include(router.urls)),#post
]
'''