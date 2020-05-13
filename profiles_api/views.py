from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication #it will generate a random token string whne the user login 
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import get_user_model

from profiles_api import serializers
from profiles_api import models
from .permissions import ProfileApiUpdatePermission, ProfileFeedUpdatePermission


# User = get_user_model()

class HelloAPiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        api_list_view =[
            'uses Http method as function (post, get, put, patch, delete)',
            'Is similar to a Django Traditional view',
            'Gives you a most control over you application logic',
            'Is mapped usually manually to urls'
        ]
        return Response({'message': 'hello', 'api_list_view': api_list_view})

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
                
class helloAPIViewset(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        api_list_view =[
            'users action (list, crrate, update, partial_update, destroy)',
            'Automatically maps to URLs using router',
            'provides more functionality ith less code',
          
        ]
        return Response({'message': 'hello', 'api_list_view': api_list_view})

        
    def create(self,request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({'message':message})
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileApiSeriallizer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (ProfileApiUpdatePermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email')


class ProfileLoginView(ObtainAuthToken):
    """Handle Creating User auth token """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES #to make it visible


class ProfilFeedViewSet(viewsets.ModelViewSet):
    """Handle Update Delete Post Serializer"""
    serializer_class = serializers.ProfileFeedSerializer
    queryset = models.Profile_Feed.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        ProfileFeedUpdatePermission,
        IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        """Override the save method to filed the current user"""    
        serializer.save(user_profile=self.request.user)
