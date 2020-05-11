from django.urls import path
from . import views
urlpatterns = [
    path('hello-api-view', views.HelloAPiView.as_view())
]