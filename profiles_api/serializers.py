from rest_framework import serializers
from django.contrib.auth import get_user_model
from profiles_api import models


# User = get_user_model()

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length = 10)


class ProfileApiSeriallizer(serializers.ModelSerializer):
    """Create a model serializer"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """Override the create function"""
        user = models.UserProfile.objects.create_user(
            name = self.validated_data['name'],
            email = self.validated_data['email'],
            password = self.validated_data['password']
        )
        return user


class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile_Feed
        fields = ('id','user_profile','status_text','created_date')
        extra_kwargs = {
            'user_profile':{'read_only':True}
        }