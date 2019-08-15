from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Image, Comment, Like
from .serializers import ImageSerializer, CountImageSerializer, CommentSerializer, LikeSerializer


class Feed(APIView):
    def get(self, request, format=None):
        user = request.user
        following_users = user.following.all()
        image_list = []

        for following_user in following_users:
            user_images = list(following_user.image_set.all()[:2])

            for image in user_images:
                image_list.append(image)

        sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)
        serializer = ImageSerializer(sorted_list, many=True)


        return Response(serializer.data)

class Search(APIView):
    def get(self, request, format=None):
        print(request.query_params)

        hashtags = request.query_params.get('hashtags', None)
        if hashtags is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        hashtags = hashtags.split(",")
        images = Image.objects.filter(tags__name__in=hashtags).distinct()

        serializer = CountImageSerializer(images, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

