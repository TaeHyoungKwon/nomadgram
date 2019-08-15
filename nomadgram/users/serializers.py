from rest_framework import serializers
from nomadgram.users.models import User
from nomadgram.images.serializers import CountImageSerializer


class UserProfileSerializer(serializers.ModelSerializer):

    image_set = CountImageSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'following_count',
            'followers_count',
            'image_set'
        )

class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'profile_image',
            'username',
            'name'
        )
