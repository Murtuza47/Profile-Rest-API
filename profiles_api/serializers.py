from rest_framework import serializers
from django.contrib.auth import get_user_model



User = get_user_model()

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length = 10)


class ProfileApiSeriallizer(serializers.ModelSerializer):
    """Create a model serializer"""
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """Override the create function"""
        user = User.objects.create_user(
            name = self.validated_data['name'],
            email = self.validated_data['email'],
            password = self.validated_data['password']
        )
        return user