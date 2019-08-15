from rest_framework import serializers
from .models import Image, Comment, Like
from nomadgram.users.models import User


class UserProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count'
        )


class FeedUserSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = User
        fields = (
            'username',
            'profile_image'
        )

class CommentSerializer(serializers.ModelSerializer):
    """
    이미지 모델 직렬화를 위한 클래스
    """
    creator = FeedUserSerializer()

    class Meta:
        model = Comment
        fields = (
            'id',
            'message',
            'creator'
        )


class LikeSerializer(serializers.ModelSerializer):
    """
    좋아요 모델 직렬화를 위한 클래스
    """
    class Meta:
        model = Like
        fields = '__all__'



class ImageSerializer(serializers.ModelSerializer):
    """
    이미지 모델 직렬화를 위한 클래스
    """
    comment_set = CommentSerializer(many=True)
    creator = FeedUserSerializer()

    class Meta:
        model = Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comment_set',
            'creator',
            'like_count',
        )

