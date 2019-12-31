from rest_framework import serializers
from django.contrib.auth import get_user_model

from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing API View"""
    name = serializers.CharField(max_length=10)


class UserProfilesSerializer (serializers.ModelSerializer):
    """Serializes a User Profile model"""

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'email',
            'password'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
