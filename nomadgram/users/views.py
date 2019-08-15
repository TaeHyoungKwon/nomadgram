from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from nomadgram.users.serializers import ListUserSerializer, UserProfileSerializer
from nomadgram.users.models import User


class ExplorerUsers(APIView):

    def get(self, request, format=None):
        last_five = User.objects.order_by('-date_joined')
        serializer = ListUserSerializer(last_five, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class FollowUser(APIView):

    def post(self, request, user_id, format=None):
        user = request.user

        try:
            user_to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.following.add(user_to_follow)
        user.save()

        return Response(status=status.HTTP_200_OK)


class UnFollowUser(APIView):

    def post(self, request, user_id, format=None):
        user = request.user

        try:
            user_to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.following.remove(user_to_follow)
        user.save()

        return Response(status=status.HTTP_200_OK)


class UserProfile(APIView):
    def get(self, request, username, format=None):

        try:
            found_user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(found_user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserFollowers(APIView):

    def get(self, request1, username, format=None):
        try:
            found_user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_followers = found_user.followers.all()
        serializer = ListUserSerializer(user_followers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserFollowing(APIView):

    def get(self, request1, username, format=None):
        try:
            found_user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_followers = found_user.following.all()
        serializer = ListUserSerializer(user_followers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


