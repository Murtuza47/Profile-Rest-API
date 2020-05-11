from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloAPiView(APIView):
    def get(self,request,format=None):
        api_list_view =[
            'uses Http method as function (post, get, put, patch, delete)',
            'Is similar to a Django Traditional view',
            'Gives you a most control over you application logic',
            'Is mapped usually manually to urls'
        ]
        return Response({'message': 'hello', 'api_list_view': api_list_view})
