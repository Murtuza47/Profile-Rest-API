from django.urls import path,include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('hello-api-viewset',views.helloAPIViewset, base_name='hello-api-viewset')
router.register('profile', views.ProfileApiViewSet,base_name='profile_querryset')
router.register('profile-feed', views.ProfilFeedViewSet,base_name='profile_feed')

urlpatterns = [
    path('hello-api-view', views.HelloAPiView.as_view()),
    path('login/',views.ProfileLoginView.as_view()),
    path('',include(router.urls))
]